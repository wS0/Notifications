import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')
# initialize the celery
app = Celery('notifications')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
