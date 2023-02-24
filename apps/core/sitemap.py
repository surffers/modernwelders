from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['privacy', 'sponsors', 'price']

    def location(self, item):
        return reverse(item)