# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from .custom_user_models import CustomUser

class Notification(models.Model):
    """
    Model to store notifications for users.
    """
    class Meta:
        db_table = "own_models_notification"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-created_at']

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications", verbose_name="User")
    title = models.CharField("Title", max_length=255)
    message = models.TextField("Message")
    is_read = models.BooleanField("Is Read", default=False)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.title}"