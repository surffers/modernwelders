from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from django.db.models import Sum, Case, When, Value


class Category(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='bookmarks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=555, blank=True, null=True)
    url = models.URLField()
    url_icon = models.URLField(blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)  # same like models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(related_name='tags')
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    number_of_votes = models.IntegerField(default=1)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return self.title


class Vote(models.Model):
    bookmark = models.ForeignKey(Bookmark, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.bookmark.number_of_votes = self.bookmark.number_of_votes + 1
        self.bookmark.save()

        super(Vote, self).save(*args, **kwargs)


class Comment(models.Model):
    bookmark = models.ForeignKey(Bookmark, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Comments'





