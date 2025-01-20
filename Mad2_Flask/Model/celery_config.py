from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['result_backend'],
        broker=app.config['broker_url']
    )
    celery.conf.update(app.config)
    celery.conf.update(
        timezone='Asia/Kolkata',
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        broker_connection_retry_on_startup=True
    )
    return celery
