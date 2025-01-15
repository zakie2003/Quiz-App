from datetime import datetime, timedelta
from flask import Blueprint,jsonify,request,session
from sqlalchemy import and_
import jwt
from Model.DataBase import db
from flask_session import Session
from Model.Model import Admin,Subject,Chapter,Quiz,Question,User

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