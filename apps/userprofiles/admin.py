from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile, Link


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'id',
        'bio',
    )

admin.site.register(Profile, ProfileAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'url',
        'user',
    )
    search_fields = (
        'url',
    )
    date_hierarchy = ('created_at')

admin.site.register(Link, LinkAdmin)