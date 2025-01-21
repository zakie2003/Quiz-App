from celery import Celery
from flask_mail import Mail

def make_celery(app):
    mail = Mail(app)
    celery = Celery(app.import_name, backend=app.config['result_backend'], broker=app.config['broker_url'])
    celery.conf.update(app.config)
    celery.conf.update(
        timezone='Asia/Kolkata',
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        broker_connection_retry_on_startup=True
    )

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return (mail, celery)


# celery -A app.celery beat --loglevel=info
# celery -A app.celery worker --loglevel=info