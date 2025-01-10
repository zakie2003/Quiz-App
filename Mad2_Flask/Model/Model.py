from Model.DataBase import db

class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    profile_url = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    token=db.Column(db.String(100), nullable=True)
    
    def __init__(self, name, profile_url, email, password, dob, token):
        self.name = name
        self.profile_url = profile_url
        self.email = email
        self.password = password
        self.dob = dob
        self.token=""
        
    def __repr__(self):
        return '<Admin %r>' % self.name
    
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    profile_url = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    qualification = db.Column(db.String(50), nullable=False)

    def __init__(self, name, profile_url, email, password, dob, qualification):
        self.name = name
        self.profile_url = profile_url
        self.email = email
        self.password = password
        self.dob = dob
        self.qualification = qualification
    
    def __repr__(self):
        return '<User %r>' % self.name


class Subject(db.Model):
    __tablename__ = "subject"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String(200),nullable=False)

    def __init__(self,name,description):
        self.name=name
        self.description=description

    def __repr__(self):
        return '<Chapter %r>' % self.name
    
class Chapter(db.Model):
    __tablename__ = "chapter"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    subject_id=db.Column(db.Integer,nullable=False)
    number_of_questions=db.Column(db.Integer,nullable=False)

    def __init__(self,name,subject_id,number_of_questions):
        self.name=name
        self.subject_id=subject_id
        self.number_of_questions=number_of_questions

    def __repr__(self):
        return '<Chapter %r>' % self.name

class Quiz(db.Model):
    __tablename__= "quiz"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    quiz_name=db.Column(db.String(50),nullable=False)
    chapter_name=db.Column(db.String(50),nullable=False)
    date_of_quiz=db.Column(db.Date,nullable=False)
    remark=db.Column(db.String(100),nullable=True)
    time_duration=db.Column(db.String(20),nullable=False)
    def __init__(self,quiz_name,chapter_name,date_of_quiz,remark,time_duration):
        self.quiz_name=quiz_name
        self.chapter_name=chapter_name
        self.date_of_quiz=date_of_quiz
        self.remark=remark
        self.time_duration=time_duration

    def __repr__(self):
        return '<Quiz %r>' % self.chapter_id


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chapter_name = db.Column(db.String(50), nullable=False)
    quiz_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(200), nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(200), nullable=False)
    def __init__(self, chapter_name,quiz_id, question, option_a, option_b, option_c, option_d, correct_option):
        self.chapter_name = chapter_name
        self.quiz_id = quiz_id
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_option = correct_option

    def __repr__(self):
        return '<Question %r>' % self.chapter_id

