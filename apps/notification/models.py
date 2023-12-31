from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    MESSAGE = 'message'
    FOLLOWER = 'follower'
    VOTE = 'vote'
    MENTION = 'mention'

    CHOICES = (
        (MESSAGE, 'Message'),
        (FOLLOWER, 'Follower'),
        (VOTE, 'Vote'),
        (MENTION, 'Mention')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']