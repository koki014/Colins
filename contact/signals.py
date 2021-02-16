from account.forms import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from django.core.mail import send_mail



@receiver(post_save, sender=Contact)
def send_form(sender, instance, **kwargs):
    subject = instance.subject
    name = instance.name
    email = instance.email
    tel_number = instance.tel_number
    sub_subject = instance.sub_subject
    message = instance.message

    user_form = f'''
        Subject: {subject} 
        Name: {name}
        Email: {email}
        Telefon: {tel_number}
        Sub subject: {sub_subject}
        Message: {message}
    '''

    send_mail(subject, user_form, 'tech.academy.docker@gmail.com', ['koki.suleymanov@mail.ru'])
    
