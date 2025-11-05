from django.db import models


class Notification(models.Model):
    STATUS = [('pending', 'Pending'),
              ('sent', 'Sent'),
              ('failed', 'Failed')]
    user_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
