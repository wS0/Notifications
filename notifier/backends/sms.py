from twilio.rest import Client
from django.conf import settings


def send(phone, _, message):
    try:
        Client(settings.TWILIO_SID, settings.TWILIO_TOKEN).messages.create(
            body=message, from_=settings.TWILIO_FROM, to=phone)
        return True, None
    except Exception as e:
        return False, str(e)
