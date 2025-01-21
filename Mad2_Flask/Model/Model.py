from Model.DataBase import db
from datetime import datetime
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


class ReadyQuiz(db.Model):
    __tablename__= "readyquiz"
    id=db.Column(db.Integer,primary_key=True)
    quiz_name=db.Column(db.String(50),nullable=False)
    chapter_name=db.Column(db.String(50),nullable=False)
    date_of_quiz=db.Column(db.Date,nullable=False)
    remark=db.Column(db.String(100),nullable=True)
    time_duration=db.Column(db.String(20),nullable=False)
    def __init__(self,id,quiz_name,chapter_name,date_of_quiz,remark,time_duration):
        self.id=id
        self.quiz_name=quiz_name
        self.chapter_name=chapter_name
        self.date_of_quiz=date_of_quiz
        self.remark=remark
        self.time_duration=time_duration

    def __repr__(self):
        return '<readyquiz %r>' % self.chapter_id

class Quiz_Library(db.Model):
    __tablename__ = "quiz_library"
    quiz_library_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,nullable=False)
    quiz_id=db.Column(db.Integer,nullable=False)
    def __init__(self,user_id,quiz_id):
        self.user_id=user_id
        self.quiz_id=quiz_id

    def __repr__(self):
        return '<readyquiz %r>' % self.quiz_library_id
    

class QuizSession(db.Model):
    quizsession_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    end_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, quiz_id, end_time):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.start_time = datetime.now()
        self.end_time = end_time
    
    def __respr__(self):
        return '<readyquiz %r>' % self.quizsession_id
    
class Score(db.Model):
    score_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,nullable=False)
    quiz_id=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date,nullable=False)
    score=db.Column(db.Integer,nullable=False)
    time=db.Column(db.Time,nullable=False)
    def __init__(self,user_id,quiz_id,score,date,time):
        self.user_id=user_id
        self.quiz_id=quiz_id
        self.score=score
        self.date=date
        self.time=time
    def __respr__(self):
        return '<readyquiz %r>' % self.score_id

class UserAnswerHistory(db.Model):
    __tablename__ = "user_answer_history"
    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    user_answer = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    date_of_attempt = db.Column(db.Date, nullable=False)
    time_of_attempt = db.Column(db.Time, nullable=False)

    def __init__(self, date_of_attempt,time_of_attempt,user_id, quiz_id, question_id, user_answer, correct_answer):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.user_answer = user_answer
        self.correct_answer = correct_answer
        self.date_of_attempt = date_of_attempt
        self.time_of_attempt = time_of_attempt

    def __repr__(self):
        return '<UserAnswerHistory %r>' % self.history_id