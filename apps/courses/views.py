from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from apps.bookmark.forms import CategoryForm, BookmarkForm, CommentForm
from apps.bookmark.models import Category, Bookmark, Comment
from apps.userprofiles.models import Profile
from taggit.models import Tag
import datetime
from django.contrib import messages


def courses(request):
    # userids = [request.user.id]
    # bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('category')
    all_categories = Category.objects.all().select_related('user')
    user_bookmarks = Bookmark.objects.all().select_related('category')
    categories = Category.objects.all()

    paginator = Paginator(user_bookmarks, 99)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user_bookmarks': user_bookmarks,
        'all_categories': all_categories,
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'courses/courses.html', context)