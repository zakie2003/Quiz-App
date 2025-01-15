from flask import Flask
from Controller.AdminController import adminbp
from Controller.UserController import userbp
from Model.DataBase import db
from flask_cors import CORS
from flask_session import Session
from redis import Redis

app=Flask(__name__)
CORS(app)
app.register_blueprint(adminbp, url_prefix='/admin')
app.register_blueprint(userbp, url_prefix='/user')

db_name = 'quiz.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config["SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(
    host='redis-19427.c322.us-east-1-2.ec2.redns.redis-cloud.com',
    port=19427,
    password="v8xa7rg4kI2YvqlL4g9wYLTFScllIiVP",
    decode_responses=False  
)
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
Session(app)

db.init_app(app)

if(__name__=="__main__"):
    with app.app_context():
        db.create_all()
    app.run(debug=True)