from datetime import datetime, timedelta
from flask import Blueprint,jsonify,request
from sqlalchemy import and_
import jwt
from Model.DataBase import db
from Model.Model import Admin,Subject,Chapter,Quiz

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
        db.session.commit()
        return jsonify({'status':200,'token':token,"id":admin_data[0].id,"email":admin_data[0].email,"name":admin_data[0].name,"password":admin_data[0].password,"message":"Admin found"})
    else:
        return jsonify({'status':404,"message":"Admin not found"})
    
@adminbp.route('/getinfo',methods=['POST'])
def getinfo():
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
        quizes=Quiz.query.all()
        temp=[]
        for i in quizes:
            row=row2dict(i)
            temp.append(row)
        return jsonify({"status":200,"quiz_data":temp})
    except Exception as e:
        return jsonify({"status":404,"message":f"{e}"})