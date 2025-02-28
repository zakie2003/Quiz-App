import os
import logging
from Model.celery_config import make_celery
from celery.schedules import crontab
from flask_mail import Mail, Message
from flask import current_app, request,send_file
from dotenv import load_dotenv
from Model.Model import UserAnswerHistory,User,Score,Question
import csv
import datetime
load_dotenv()

def init_tasks(celery):

    @celery.task(name='add')
    def add():
        print("ADDing")
        return "Triggring"
    
    @celery.task(name="get_csv_data")
    def get_csv_data(user_id,quiz_id,date,time):
        try:
            user_anserhistory=UserAnswerHistory.query.filter(UserAnswerHistory.user_id==user_id,UserAnswerHistory.quiz_id==quiz_id,UserAnswerHistory.date_of_attempt==date,UserAnswerHistory.time_of_attempt==time).all()
            for answer in user_anserhistory:
                print(answer.user_id,answer.quiz_id,answer.question_id,answer.user_answer,answer.correct_answer)
            file_path = 'user_answer_history.csv'
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['User_id', 'Quiz_id', 'Question_id','Question Description', 'User_answer', 'Correct_answer'])
                for answer in user_anserhistory:
                    question_description=Question.query.filter(Question.id==answer.question_id,Question.quiz_id==answer.quiz_id).first().question
                    writer.writerow([answer.user_id, answer.quiz_id, answer.question_id,question_description, answer.user_answer, answer.correct_answer])
            return file_path
        except Exception as e:
            print(e)

    @celery.task(name="send_monthy_report")
    def send_monthy_report():
        try:
            logging.info("Attempting to send email...")
            mail = Mail(current_app)
            sender_email = os.getenv("EMAIL")
            end_date = datetime.datetime.now()
            start_date = end_date - datetime.timedelta(days=30)

            users = User.query.all()

            for user in users:

                quizzes = Score.query.filter(
                    Score.user_id == user.id,
                    Score.date >= start_date,
                    Score.date <= end_date
                ).all()

                if not quizzes:
                    continue  

                report_text = f"Hello {user.name},\n\nHere is your monthly quiz performance summary:\n\n"

                for quiz in quizzes:
                    report_text += f"Date: {quiz.date},Quiz: {quiz.quiz_id}, Score: {quiz.score}\n"

                report_text += "\nKeep up the good work!\n\nBest Regards,\nYour Quiz Team"

                msg = Message("Your Monthly Quiz Report", sender=sender_email, recipients=[user.email])
                msg.body = report_text
                mail.send(msg)

            return "Monthly reports successfully sent"
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            return f"Failed to send email: {e}"

    @celery.task(name='send_mail')
    def send_mail(text):
        print("send_mail task started")
        with current_app.app_context():
            try:
                logging.info("Attempting to send email...")
                mail = Mail(current_app)
                sender_email = os.getenv("EMAIL")
                
                html_content = f"""
                <html>
                    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                        <h2 style="color: #2c3e50;">Your Daily Challenge Awaits! 🌟</h2>
                        <p>Ready to test your knowledge and level up your skills? 🎓</p>
                        <p>Your daily quiz is live! Here's your chance to:</p>
                        <ul>
                            <li>Sharpen your mind.</li>
                            <li>Earn points and climb the leaderboard.</li>
                            <li>Track your progress over time.</li>
                        </ul>
                        <p>
                            <a href="https://zingy-gelato-29d699.netlify.app" 
                            style="background-color: #4CAF50; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px;">
                            Take Today's Quiz
                            </a>
                        </p>
                        <p>Happy Quizzing!<br>The MindSpark Team</p>
                    </body>
                </html>
                """
                user_email=User.query.all()
                mails=[]
                for i in user_email:
                    mails.append(i.email)
        
                msg = Message("Your Daily Challenge Awaits! 🌟 Take Today's Quiz Now",
                            sender=sender_email,
                            recipients=mails)
                msg.body = text  
                msg.html = html_content  
                mail.send(msg)

                print("Mail successfully sent by Celery")
                return "Mail successfully sent by Celery"
            except Exception as e:
                logging.error(f"Failed to send email: {e}")
                return f"Failed to send email: {e}"
            


    celery.conf.beat_schedule = {
        "email-task": {
            "task": "send_mail",
            'schedule': crontab(day_of_month='*', hour=10, minute=0),
            "args": (
                """Ready to test your knowledge and level up your skills? 🎓
                    Your daily quiz is live! Here's your chance to:
                        - Sharpen your mind.
                        - Earn points and climb the leaderboard.
                        - Track your progress over time.""",
            )
        },
        "send-monthly-report": {
            "task": "send_monthy_report",
            'schedule': crontab(day_of_month=1, hour=10),
        }
    }
    celery.conf.timezone = 'Asia/Kolkata'
