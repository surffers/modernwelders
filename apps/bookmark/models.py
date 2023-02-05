from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db.models import Sum, Case, When, Value
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="slug", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='bookmarks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=555, blank=True, null=True)
    url = models.URLField()
    url_icon = models.URLField(blank=True, null=True)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(related_name='tags')
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    number_of_votes = models.IntegerField(default=1)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def total_views(self):
        return self.views.count()

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
    body = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Comments'






