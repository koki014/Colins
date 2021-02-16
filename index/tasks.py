from index.models import Subscriber, Follow
import time
from celery import shared_task
from django.template.loader import render_to_string
from instapi import Client
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from account.tools.tokens import account_activation_token

@shared_task
def dump_database():
    print('database dump olunmaga basladi')
    time.sleep(60)
    print('database dump olundu')


@shared_task
def send_mail_to_subscribes():
    subscriber_emails = Subscriber.objects.values_list('email', flat=True)
    context = {
        'site_address': settings.SITE_ADDRESS,
    }

    html_message = render_to_string('email/email.subscribes.html', context)
    subject = 'News About our site'

    email = EmailMessage(subject=subject, body=html_message, from_email=settings.EMAIL_HOST_USER, to=subscriber_emails)
    email.content_subtype = 'html'
    email.send()


@shared_task
def instagram():
    user_name = '_slymnov_'
    password = '0703331409Nizi'
    api = Client(user_name, password)
    results = api.user_feed('297887086')
    items = results.get('items', [])
    data = Follow.objects.all()
    data.delete()
    for item in items:
        image = item['image_versions2']['candidates'][0]['url']
        title = item['code']
        url = 'https://www.instagram.com/p/'
        
        Follow.objects.create(image=image, title=f'{url}{title}')