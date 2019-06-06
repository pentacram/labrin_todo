from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from django.utils import timezone
from .models import Todo

@shared_task
def mul(x, y):
    print(x*y)
    return x * y



@shared_task
def send_email():
    tooday = datetime.date.today()
    data = Todo.objects.filter(deaddate=tooday)
    timea = data.objects.filter()


