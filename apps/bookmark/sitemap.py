from django.contrib.sitemaps import Sitemap
from .models import Category, Bookmark
from django.shortcuts import reverse


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class BookmarkSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Bookmark.objects.all()

    def lastmod(self, obj):
        return obj.created_at

