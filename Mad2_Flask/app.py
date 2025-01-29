import os
import logging
from flask import Flask, jsonify,request, send_file
from Controller.AdminController import adminbp
from Controller.UserController import userbp
from Model.DataBase import db
from flask_cors import CORS
from flask_session import Session
from flask_mail import Mail,Message
from redis import Redis
from Model.celery_config import make_celery
from Model.tasks import init_tasks
from flask_caching import Cache
from Model.cache_config import cache
from Model.Model import user_otp
app = Flask(__name__)

# Initialize CORS with proper configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

cache.init_app(app)


app.register_blueprint(adminbp, url_prefix='/admin')
app.register_blueprint(userbp, url_prefix='/user')

db_name = 'quiz.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config["SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(
    host='redis-19427.c322.us-east-1-2.ec2.redns.redis-cloud.com',port=19427,
    password="v8xa7rg4kI2YvqlL4g9wYLTFScllIiVP",decode_responses=False)
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'

app.config['broker_url'] = 'redis://:v8xa7rg4kI2YvqlL4g9wYLTFScllIiVP@redis-19427.c322.us-east-1-2.ec2.redns.redis-cloud.com:19427/0'
app.config['result_backend'] = 'redis://:v8xa7rg4kI2YvqlL4g9wYLTFScllIiVP@redis-19427.c322.us-east-1-2.ec2.redns.redis-cloud.com:19427/0'

# Configure logging
logging.basicConfig(level=logging.INFO)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("EMAIL")  

mail,celery = make_celery(app)
init_tasks(celery)

@app.route("/celery/add", methods=["GET"])
def celery_add():
    result = celery.tasks['add'].delay()
    return jsonify(result=result.get())

@app.route("/celery/get_csv_data", methods=["GET"])
def celery_get_csv_data():
    user_id = request.args.get('user_id')
    quiz_id = request.args.get('quiz_id')
    date=request.args.get('date')
    time=request.args.get('time')
    result = celery.tasks['get_csv_data'].delay(user_id=user_id, quiz_id=quiz_id,date=date,time=time)
    file_path = result.get()
    return send_file(file_path, as_attachment=True)

@app.route("/user/send_otp",methods=["POST"])
def save_otp():
    try:
        data=request.json
        otp=data["otp"]
        email=data["email"]
        user=user_otp.query.filter_by(email=email).first()
        if user:
            user.otp=otp
            db.session.commit()
            mail=Mail(app)
            msg=Message("OTP Verification",sender=os.environ.get("EMAIL"),recipients=[email],body=f"Your OTP is {otp}")
            mail.send(msg)
            
            return jsonify({"status":200,"message":"OTP updated"})
        otp=user_otp(email=email,otp=otp)
        db.session.add(otp)
        db.session.commit()
        mail=Mail(app)
        msg=Message("OTP Verification",sender=os.environ.get("EMAIL"),recipients=[email],body=f"Your OTP is {otp.otp}")
        mail.send(msg)
        
        return jsonify({"status":200,"message":"OTP saved"})
    except Exception as e:
        return jsonify({"status":500,"message":f"{e}"})

Session(app)
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,use_reloader=True)