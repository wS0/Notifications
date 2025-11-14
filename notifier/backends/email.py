from django.core.mail import send_mail
from django.conf import settings


def send(user_email, title, message):
    try:
        send_mail(title, message, settings.DEFAULT_FROM_EMAIL, [user_email])
        return True, None
    except Exception as e:
        return False, str(e)
