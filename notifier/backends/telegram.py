import requests
from django.conf import settings


def send(chat_id, title, message):
    try:
        requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            data={'chat_id': chat_id, 'text': f"*{title}*\n\n{message}", 'parse_mode': 'Markdown'}
        ).raise_for_status()
        return True, None
    except Exception as e:
        return False, str(e)
