from datetime import datetime, timedelta
from flask import Blueprint,jsonify,request,session
from sqlalchemy import and_
import jwt
from Model.DataBase import db
from flask_session import Session
from Model.Model import Admin,Subject,Chapter,Quiz,Question,ReadyQuiz,User

adminbp=Blueprint('adminbp',__name__)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

@adminbp.route("/create")
def create():
    dob = datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    data=Admin("admin","","admin@gmail.com","1234",dob,"")
    db.session.add(data)
    db.session.commit()
    return "Admin created"

@adminbp.route('/authorize',methods=['GET','POST'])
def authorize():
    data=request.json
    admin_data=Admin.query.filter(and_(Admin.email==data['email'], Admin.password==data['password'])).all()
    # print(admin_data)
    if(len(admin_data)>0):
        token = jwt.encode({'user_id': admin_data[0].id,'exp': datetime.now() + timedelta(hours=1)}, "secret", algorithm='HS256')
        admin_data[0].token=token
        session["token"] = token
        session["name"] = admin_data[0].name
        db.session.commit()
        return jsonify({'status':200,'token':token,"id":admin_data[0].id,"email":admin_data[0].email,"name":admin_data[0].name,"password":admin_data[0].password,"message":"Admin found"})
    else:
        return jsonify({'status':404,"message":"Admin not found"})
    
@adminbp.route('/getinfo',methods=['POST'])
def getinfo():
    if(session.get("token") is None):
        return jsonify({'status':404,"message":"Admin not found"})
    data = request.json
    token = data["token"][1:len(data["token"])-1]
    admin_data = Admin.query.filter(Admin.token == token).all()
    if len(admin_data) > 0:
        admin_info = {
            'id': admin_data[0].id,
            'name': admin_data[0].name,
            'email': admin_data[0].email,
            'token': admin_data[0].token
        }
        return jsonify({'status': 200, 'data': admin_info})
    else:
        return jsonify({'status': 404, "message": "Admin not found"})
    
@adminbp.route("/get_subject")
def get_subjects():
    try:
        subject=Subject.query.all()
        subject_list=[]
        for chapter in subject:
             subject_list.append(row2dict(chapter))
        return jsonify({"status":200,"data":subject_list})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})

@adminbp.route("/add_subject",methods=['POST'])
def create_subject():
    try:
        data=request.json
        subject=Subject(data["name"],data["description"])
        db.session.add(subject)
        db.session.commit()
        return jsonify({"status":200,"message":"Subject created"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})


@adminbp.route("/add_chapter",methods=['POST'])
def create_chapter():
    try:
        data=request.json
        print(data["name"],data["subject_id"],data["numberofquestion"])
        chapter=Chapter(data["name"],data["subject_id"],data["numberofquestion"])

        db.session.add(chapter)
        db.session.commit()
        return jsonify({"status":200,"message":"Chapter created"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/get_chapter",methods=['GET'])
def get_chapters():
    try:
        subject_id=request.args.get("subject_id")
        if(subject_id==None):
            chapter=Chapter.query.all()
        else:
            chapter=Chapter.query.filter(Chapter.subject_id==subject_id).all()
        chapter_list=[]
        for chapter in chapter:
             chapter_list.append(row2dict(chapter))
        return jsonify({"status":200,"data":chapter_list})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/edit_chapter",methods=['POST'])
def edit_chapter():
    try:
        data=request.json
        chapter=Chapter.query.filter(Chapter.name==data["name"]).first()
        question=Question.query.filter(Question.chapter_name==data["name"]).all()
        if(len(question)>data["numberofquestion"]):
            return jsonify({"status":404,"message":"Can't edit number of question"})

        chapter.name=data["name"]
        chapter.number_of_questions=data["numberofquestion"]
        db.session.commit()
        return jsonify({"status":200,"message":"Chapter edited"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/delete_chapter",methods=['GET'])
def delete_chapter():
    try:
        chapter=Chapter.query.filter(Chapter.name==request.args.get("name")).first()
        db.session.delete(chapter)
        db.session.commit()
        return jsonify({"status":200,"message":"Chapter deleted"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/add_quiz",methods=["POST"])
def add_quiz():
    try:
        data=request.json
        date = datetime.strptime(data["date_of_conduction"], "%Y-%m-%d").date()
        quiz=Quiz(quiz_name=data["quiz_name"],chapter_name=data["chapter_name"],date_of_quiz=date,time_duration=data["duration"],remark=data["remark"])
        db.session.add(quiz)
        db.session.commit()
        return jsonify({"status":200,"message":"Request Sent"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/get_quizes")
def get_quizes():
    try:
        quizes = Quiz.query.all()
        ready_quiz_ids = {quiz.id for quiz in ReadyQuiz.query.all()}
        temp = []
        for quiz in quizes:
            if quiz.id not in ready_quiz_ids:
                row = row2dict(quiz)
                temp.append(row)
        return jsonify({"status": 200, "quiz_data": temp})
    except Exception as e:
        return jsonify({"status": 404, "message": f"{e}"})

@adminbp.route("/get_ready_quizes",methods=["GET"])  
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

@adminbp.route("/add_ready_quiz", methods=["POST"])
def add_ready_quiz():
    try:
        data = request.json
        id = data["quiz_id"]
        existing_quiz = Quiz.query.filter(Quiz.id == id).first()
        if existing_quiz is None:
            return jsonify({"status": 404, "message": "Quiz not found"})
        
        date_str = existing_quiz.date_of_quiz.strftime("%Y-%m-%d")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        ready_quiz = ReadyQuiz(
            id=id,
            quiz_name=existing_quiz.quiz_name,
            chapter_name=existing_quiz.chapter_name,
            date_of_quiz=date,
            time_duration=existing_quiz.time_duration,
            remark=existing_quiz.remark
        )
        db.session.add(ready_quiz)
        db.session.commit()
        return jsonify({"status": 200, "message": "Request Sent"})
    except Exception as e:
        print(e)
        return jsonify({"status": 404, "message": str(e)})

@adminbp.route("/remove_ready_quiz", methods=["POST"])
def remove_ready_quiz():
    try:
        data = request.json
        id = data["quiz_id"]
        ready_quiz = ReadyQuiz.query.filter(ReadyQuiz.id == id).first()
        if ready_quiz is None:
            return jsonify({"status": 404, "message": "Ready Quiz not found"})
        
        db.session.delete(ready_quiz)
        db.session.commit()
        return jsonify({"status": 200, "message": "Ready Quiz removed"})
    except Exception as e:
        return jsonify({"status": 404, "message": str(e)})

@adminbp.route("/add_question",methods=["POST"])
def add_question():
    try:
        data=request.json
        prev_question=Question.query.filter(Question.chapter_name==data["chapter_name"],Question.quiz_id==data["quiz_id"]).all()
        chapter=Chapter.query.filter(Chapter.name==data["chapter_name"]).first()    
        number_of_questions=chapter.number_of_questions
        if(len(prev_question)>=number_of_questions):
            return jsonify({"status":404,"message":"Question limit reached"})
        
        question=Question(data["chapter_name"],data["quiz_id"],data["question_description"],data["option_1"],data["option_2"],data["option_3"],data["option_4"],data["answer"])
        db.session.add(question)
        db.session.commit()
        return jsonify({"status":200,"message":"Question Added"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    

@adminbp.route("/get_questions",methods=["POST"])
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
    
@adminbp.route("/get_question",methods=["POST"])
def get_question():
    try:
        data=request.json
        question=Question.query.filter(Question.id==data["question_id"]).first()
        row=row2dict(question)
        return jsonify({"message":"Got Question","data":row,"status_code":"200"})
    except Exception as e:
        return jsonify({"error":f"{e}","status_code":"404"})
    
@adminbp.route("/delete_question",methods=["POST"])
def delete_question():
    try:
        data=request.json
        question=Question.query.filter(Question.id==data["id"]).first()
        db.session.delete(question)
        db.session.commit()
        return jsonify({"status":200,"message":"Question Deleted"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})
    
@adminbp.route("/edit_question",methods=["POST"])
def edit_question():
    try:
        data=request.json
        question=Question.query.filter(Question.id==data["id"]).first()
        print(data)
        question.question=data["question_description"]
        question.option_a=data["option_1"]
        question.option_b=data["option_2"]
        question.option_c=data["option_3"]
        question.option_d=data["option_4"]
        question.correct_option=data["correct_option"]
        db.session.commit()
        return jsonify({"status":200,"message":"Question edited"})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})

@adminbp.route("/get_quiz",methods=["POST"])
def get_quiz():
    data=request.json
    quiz=Quiz.query.filter(Quiz.id==data["quiz_id"]).first()
    if(quiz is None):
        return jsonify({"status":404,"message":"quiz not found"})
    return jsonify({"status":200,"quiz":row2dict(quiz)})

@adminbp.route("/search", methods=["POST"])
def search():
    try:
    
        search_term = request.json["search"]
        print(search_term)
        user = User.query.filter(User.name.ilike(f"%{search_term}%")).all()
        quiz = Quiz.query.filter(Quiz.quiz_name.ilike(f"%{search_term}%")).all()
        subjects = Subject.query.filter(Subject.name.ilike(f"%{search_term}%")).all()
        user_list = [row2dict(u) for u in user]
        quiz_list = [row2dict(q) for q in quiz]
        subject_list = [row2dict(s) for s in subjects]
        return jsonify({"status": 200, "user": user_list, "quiz": quiz_list, "subject": subject_list})
    except Exception as e:
        return jsonify({"status": 500, "Error": f"{e}"})

# Register the blueprint in the main app file
# app.register_blueprint(adminbp, url_prefix='/admin')