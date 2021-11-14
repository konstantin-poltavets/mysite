# tasks.py
# Импортируем созданный нами ранее экземпляр класса celery(app)
from mysite.celery import app
#from celery import app.tasks
from celery import shared_task

# Декоратор @app.task, говорит celery о том, что эта функция является (task-ом) т.е. должна выполнятся в фоне.



@shared_task(name="multiply_two_numbers")
def add(x, y):
    print(x*y)
    return x *y