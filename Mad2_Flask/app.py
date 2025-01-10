from flask import Flask
from Controller.AdminController import adminbp
from Model.DataBase import db
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.register_blueprint(adminbp, url_prefix='/admin')

db_name = 'quiz.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config["SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'

db.init_app(app)

if(__name__=="__main__"):
    with app.app_context():
        db.create_all()
    app.run(debug=True)