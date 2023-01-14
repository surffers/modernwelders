from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from .models import Category, Bookmark, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'user',
    )
    search_fields = (
        'title',
    )
    date_hierarchy = ('created_at')

admin.site.register(Category, CategoryAdmin)


class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'url',
        'user',
        'tag_list'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Bookmark, BookmarkAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'body',
        'created_at',
    )

admin.site.register(Comment, CommentAdmin)


    

    