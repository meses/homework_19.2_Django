from django.conf import settings
from django.core.mail import send_mail

def send_congratuation_email():
    send_mail(
        'Поздравляем!',
        'Статья набрала сто просмотров',
        settings.EMAIL_HOST_USER,
        recipient_list=['dvayuzer@yandex.ru']
    )