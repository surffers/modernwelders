from datetime import timezone, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True)

User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])


class Link(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200)
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.url