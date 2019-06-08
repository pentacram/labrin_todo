from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Todo
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def mul(x, y):
    print(x*y)
    return x * y



    
@shared_task()
def send_email(username, mail_adress):
    username = User.objects.all()
    send_mail(
        subject = "taskin bitmesine 10 deqiqe qalib" + username,
        html_message='taskin vaxti bitir',
        message="taskin bitmesine 10 deqiqe qalib",
        from_email = 'pentacram55@gmail.com',
        recipient_list = [mail_adress]
    )
    return f"Hello {username}"
    #message = EmailMessage('Subject', 'Message', to=[user.email])
    #message.send()
    print('Email is sent')

        





