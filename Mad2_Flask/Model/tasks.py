from Model.celery_config import make_celery

def init_tasks(celery):
    @celery.task(name='add')
    def add(x, y):
        return x + y
