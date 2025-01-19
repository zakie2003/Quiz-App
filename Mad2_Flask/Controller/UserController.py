from datetime import datetime, timedelta
from flask import Blueprint,jsonify,request,session
from sqlalchemy import and_
import jwt
from Model.DataBase import db
from flask_session import Session
from Model.Model import Admin,Subject,Chapter,Quiz,Question,User,ReadyQuiz,Quiz_Library,QuizSession

userbp=Blueprint('userbp',__name__)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

@userbp.route("/create_user",methods=["POST"])
def create_user():
    try:
        data=request.json
        prev_user=User.query.filter(User.email==data["email"]).first()
        if(prev_user is not None):
            return jsonify({"status":404,"message":"User already exists"})
        for(key,value) in data.items():
            if(data[key]=="" and key!="profile_url"):
                return jsonify({"status":404,"message":f"{key} is required"})
        dob = datetime.strptime(data["dob"], "%Y-%m-%d").date()
        user=User(data["name"],data["profile_url"],data["email"],data["password"],dob,data["qualification"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"status":200,"message":"User created"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
        
@userbp.route("/user_authorize",methods=["POST"])
def user_authorize():
    try:
        data=request.json
        user=User.query.filter(and_(User.email==data["email"],User.password==data["password"])).first()
        if(user is None):
            return jsonify({"status":404,"message":"User not found"})
        session["user_id"] = user.id
        token = jwt.encode({'user_id': user.id,'exp': datetime.now() + timedelta(hours=1)}, "secret", algorithm='HS256')
        session["token"] = token
        session["name"] = user.name
        return jsonify({"status":200,"password":user.password,"token":token,"name":user.name,"id":user.id,"message":"User logged in"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    

@userbp.route("/get_quizes",methods=["GET"])
def get_quizes():
    try:
        quizes=Quiz.query.all() 
        temp=[]
        for i in quizes:
            row=row2dict(i)
            temp.append(row)
        return jsonify({"status":200,"quiz_data":temp})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@userbp.route("/get_ready_quizes",methods=["GET"])  
def get_ready_quizes():
    try:
        ready_quiz=ReadyQuiz.query.all()
        temp=[]
        for i in ready_quiz:
            row=row2dict(i)
            temp.append(row)
        return jsonify({"status":200,"ready_quiz_data":temp})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@userbp.route("/add_to_library",methods=["POST"])
def add_to_library():
    try:
        data=request.json
        user=User.query.filter(User.id==data["user_id"]).first()
        ready_quiz=ReadyQuiz.query.filter(ReadyQuiz.id==data["quiz_id"]).first()
        if(user is None or ready_quiz is None):
            return jsonify({"status":404,"message":"User or Quiz not found"})
        library=Quiz_Library(user_id=user.id,quiz_id=data["quiz_id"])
        db.session.add(library)
        db.session.commit()
        return jsonify({"status":200,"message":"Quiz added to library"})
    except Exception as e:
        return jsonify({"status":500,"message":f"{e}"})

@userbp.route("/get_my_quizes",methods=["POST"])
def get_my_quizes():
    try:
        data = request.json
        user = User.query.filter(User.id == data["user_id"]).first()
        if user is None:
            return jsonify({"status": 404, "message": "User not found"})
        quiz_library = Quiz_Library.query.filter(Quiz_Library.user_id == data["user_id"]).all()
        arr = []
        for i in quiz_library:
            row = row2dict(i)
            arr.append(row)
        return jsonify({"status": 200, "quiz_library_data": arr})
    except Exception as e:
        return jsonify({"status": 500, "message": f"{e}"})

@userbp.route("/check_quiz_in_library", methods=["POST"])
def check_quiz_in_library():
    try:
        data = request.json
        print(data)
        user_id = data["user_id"]
        quiz_id = data["quiz_id"]
        
        quiz_in_library = Quiz_Library.query.filter(and_(Quiz_Library.user_id == user_id, Quiz_Library.quiz_id == quiz_id)).first()
        if quiz_in_library:
            quiz_details=Quiz.query.filter(Quiz.id==quiz_id).first()
            if(quiz_details is None):
                return jsonify({"status": 404, "message": "Quiz not found"})
            row=row2dict(quiz_details)
            return jsonify({"status": 200, "quiz_data": row,"is_in_library": True})
        else:
            return jsonify({"status": 200, "is_in_library": False})
    except Exception as e:
        return jsonify({"status": 500, "message": f"{e}"})
    
@userbp.route("/get_questions",methods=["POST"])
def get_questions():
    try:
       data=request.json
       questions=Question.query.filter(Question.chapter_name==data["chapter_name"] , Question.quiz_id==data["quiz_id"]).all()
       quest_list=[]
       for row in questions:
           row=row2dict(row)
           quest_list.append(row)
       return jsonify({"message":"Got Questions","data":quest_list,"status_code":"200"})
    except Exception as e:
        return jsonify({"error":f"{e}","status_code":"404"})

@userbp.route("/start_quiz",methods=["POST"])
def start_quiz():
    try:
        data = request.json
        print(data)
        quiz = Quiz.query.filter(Quiz.id == data["quiz_id"]).first()
        if not quiz:
            return jsonify({'error': 'Invalid quiz ID', 'status_code': '404'})
        
        expired_session = QuizSession.query.filter(and_(QuizSession.user_id == data["user_id"], QuizSession.quiz_id == data["quiz_id"]),QuizSession.end_time<datetime.now()).first()
        # print("Expired ",expired_session)
        if expired_session:
            db.session.delete(expired_session)
            db.session.commit()

        minutes, seconds = map(int, quiz.time_duration.split(':'))
        total_seconds = minutes * 60 + seconds
        start_time = datetime.now()
        end_time = datetime.now() + timedelta(seconds=total_seconds)
        current_session = QuizSession.query.filter(and_(QuizSession.user_id == data["user_id"], QuizSession.quiz_id == data["quiz_id"]),QuizSession.end_time>datetime.now()).first()
        if not current_session:
            session = QuizSession(user_id=data["user_id"], quiz_id=data["quiz_id"], end_time=end_time)
            db.session.add(session)
            db.session.commit()

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({"error": f"{e}", "status_code": "500"})
    
@userbp.route('/remaining_time', methods=['POST'])
def get_remaining_time():
    try:
        data = request.json
        user_id = data.get('user_id')
        quiz_id = data.get('quiz_id')
        session = QuizSession.query.filter(and_(QuizSession.user_id == user_id, QuizSession.quiz_id == quiz_id)).first()
        if not session:
            return jsonify({'error': 'Session not found'}), 404
        remaining_time = int((session.end_time - datetime.now()).total_seconds())
        # print("Time ",remaining_time)
        if remaining_time <= 0:
            return jsonify({'remainingTime': 0, 'status': 'Time is up'})

        return jsonify({'remainingTime': remaining_time})
    except Exception as e:
        return jsonify({'error': f'{e}', 'status_code': '500'})
    
@userbp.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    try:
        data = request.json
        user_id = data.get('user_id')
        quiz_id = data.get('quiz_id')
        print(user_id, quiz_id)
        session = QuizSession.query.filter(and_(QuizSession.user_id == user_id, QuizSession.quiz_id == quiz_id)).first()
        if not session:
            return jsonify({'error': 'Session not found'}), 404
        db.session.delete(session)
        db.session.commit()

        return jsonify({'session_deleted': True})
    except Exception as e:
        return jsonify({"error": f"{e}", "status_code": 500})