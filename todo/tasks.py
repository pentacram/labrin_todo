from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Todo
from django.core.mail import send_mail
from django.contrib.auth.models import User
from labrin import settings

@shared_task
def mul(x, y):
    print(x*y)
    return x * y



    
@shared_task()
def send_email(subject,message,recipient):
    send_mail(
        subject = subject,
        message= message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [recipient]
    )
    print('Email is sent')

        





