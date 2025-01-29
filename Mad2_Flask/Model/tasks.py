import os
import logging
from Model.celery_config import make_celery
from celery.schedules import crontab
from flask_mail import Mail, Message
from flask import current_app, request,send_file
from dotenv import load_dotenv
from Model.Model import UserAnswerHistory
import csv
load_dotenv()

def init_tasks(celery):

    @celery.task(name='add')
    def add():
        print("ADDing")
        return "Triggring"
    
    @celery.task(name="get_csv_data")
    def get_csv_data(user_id,quiz_id,date,time):
        user_anserhistory=UserAnswerHistory.query.filter(UserAnswerHistory.user_id==user_id,UserAnswerHistory.quiz_id==quiz_id,UserAnswerHistory.date_of_attempt==date,UserAnswerHistory.time_of_attempt==time).all()
        for answer in user_anserhistory:
            print(answer.user_id,answer.quiz_id,answer.question_id,answer.user_answer,answer.correct_answer)
        file_path = 'user_answer_history.csv'
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'quiz_id', 'question_id', 'user_answer', 'correct_answer'])
            for answer in user_anserhistory:
                writer.writerow([answer.user_id, answer.quiz_id, answer.question_id, answer.user_answer, answer.correct_answer])
        return file_path

    @celery.task(name="send_monthy_report")
    def send_monthy_report():
        try:
            logging.info("Attempting to send email...")
            mail = Mail(current_app)
            sender_email = os.getenv("EMAIL")
            msg = Message("Monthly Report", sender=sender_email, recipients=["sXm0g@example.com"])
            msg.body = "Monthly Report"
            mail.send(msg)
            return "Mail successfully sent by Celery"
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
                
                # Create an HTML formatted message
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
                            <a href="#" 
                            style="background-color: #4CAF50; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px;">
                            Take Today's Quiz
                            </a>
                        </p>
                        <p>Happy Quizzing!<br>The MindSpark Team</p>
                    </body>
                </html>
                """

                msg = Message("Your Daily Challenge Awaits! 🌟 Take Today's Quiz Now",
                            sender=sender_email,
                            recipients=["zak2022.khan@gmail.com"])
                msg.body = text  # Plain text fallback
                msg.html = html_content  # HTML formatted email
                mail.send(msg)

                print("Mail successfully sent by Celery")
                return "Mail successfully sent by Celery"
            except Exception as e:
                logging.error(f"Failed to send email: {e}")
                return f"Failed to send email: {e}"
            


    celery.conf.beat_schedule = {
        "email-task": {
            "task": "send_mail",
            "schedule": crontab(day_of_week="*"),
            "args": (
                """Ready to test your knowledge and level up your skills? 🎓
    Your daily quiz is live! Here's your chance to:
        - Sharpen your mind.
        - Earn points and climb the leaderboard.
        - Track your progress over time.""",
            )
        }

    }
    celery.conf.timezone = 'Asia/Kolkata'
