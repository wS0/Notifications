from celery import shared_task
from .models import Notification
from .backends import email, sms, telegram
from datetime import datetime


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def deliver(self, pk):
    n = Notification.objects.get(pk=pk)
    channels = [
        (email.send, n.user_id, n.title, n.message),  # user_id = email
        (sms.send, '+79161234567', None, n.message),
        (telegram.send, '123456789', n.title, n.message),
    ]
    for send_fn, target, title, msg in channels:
        if title is None:
            title = "Уведомление"
        ok, err = send_fn(target, title, msg)
        if ok:
            n.status = 'sent'
            n.sent_at = datetime.now()
            n.save()
            return f"Sent via {send_fn.__module__}"
        n.error = err
        n.save()
    n.status = 'failed'
    n.save()
    raise self.retry(countdown=300)
