from django.contrib.admin import filters
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from apps.bookmark.forms import CategoryForm, BookmarkForm, CommentForm
from apps.bookmark.models import Category, Bookmark, Comment
from apps.userprofiles.models import Profile
from taggit.models import Tag
import datetime
import random
from django.contrib import messages
# from datetime import datetime, timedelta


def bookmarks_filter(request, pk):
    """ Фильтр статей по дате
            """
    bookmarks = Bookmark.objects.filter(published_date__lte=timezone.now()).select_related('category')
    if pk == 1:
        now = datetime.datetime.now() - datetime.timedelta(days=7)
        bookmarks = bookmarks.filter(created_at__gte=now)
    elif pk == 2:
        now = datetime.datetime.now() - datetime.timedelta(days=30)
        bookmarks = bookmarks.filter(created_at__gte=now)
    elif pk == 3:
        bookmarks = bookmarks

    return render(request, 'core/users_links_lists.html', {"bookmarks": bookmarks})


def users_links_lists(request):
    # userids = [request.user.id]
    # bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('category')
    all_categories = Category.objects.all().select_related('user')
    bookmarks = Bookmark.objects.filter(published_date__lte=timezone.now()).select_related('category')
    categories = Category.objects.all()

    paginator = Paginator(bookmarks, 99)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bookmarks': bookmarks,
        'all_categories': all_categories,
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'core/users_links_lists.html', context)


def privacy(request):

    context = {

    }
    return render(request, 'core/privacy.html', context)


def price(request):

    context = {

    }
    return render(request, 'core/price.html', context)


def error_404_view(request, exception):
    return render(request, 'core/404.html')


@login_required
def tests(request):

    all_categories = Category.objects.all().select_related('user')

    bookmarks = Bookmark.objects.all().select_related('category').order_by("-created_at")
    categories = Category.objects.all().prefetch_related('bookmarks', 'user')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('/')

    paginator = Paginator(bookmarks, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bookmarks': bookmarks,
        'all_categories': all_categories,
        'page_obj': page_obj,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/tests.html', context)


def home(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=7)
    # tags = Tag.objects.all().order_by()[0:3]
    tags = Tag.objects.order_by('?')[0:30]
    random.choice(Tag.objects.all())

    comments = Comment.objects.all().order_by("-created_at")[0:1]
    profiles = Profile.objects.all().order_by("-created")
    home_categories = Category.objects.filter(published_date__lte=timezone.now()).prefetch_related('bookmarks', 'user').order_by("-created_at")[0:10]
    bookmarks = Bookmark.objects.filter(published_date__lte=timezone.now(), created_at__gte=date_from).select_related('category', 'user').order_by('-number_of_votes')#[0:3]
    user_categories = Category.objects.filter(published_date__lte=timezone.now())

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        messages.success(request, 'Категория создана!')
        return redirect('profile', username=request.user.username)

    paginator = Paginator(bookmarks, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'comments': comments,
        'tags': tags,
        'page_obj': page_obj,
        'profiles': profiles,
        'bookmarks': bookmarks,
        'user_categories': user_categories,
        'home_categories': home_categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/home.html', context)


def categories(request):
    userids = [request.user.id]
    all_categories = Category.objects.filter(published_date__lte=timezone.now())
    categories = Category.objects.all().select_related('user')
    published_categories = Category.objects.filter(published_date__lte=timezone.now()).select_related('user')
    bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('category', 'user')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        messages.success(request, 'Категория создана!')
        return redirect('categories')

    paginator = Paginator(categories, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bookmarks': bookmarks,
        'all_categories': all_categories,
        'page_obj': page_obj,
        'categories': categories,
        'published_categories': published_categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/dashboard.html', context)


def search(request):
    b = Bookmark.objects.filter(published_date__lte=timezone.now())
    query = request.GET.get('q', '')

    if len(query) > 0:
        bookmarks = Bookmark.objects.filter(Q(title__icontains=query, published_date__lte=timezone.now()) | Q(category__title__icontains=query))
        categories = Category.objects.filter(title__icontains=query, published_date__lte=timezone.now())

    else:
        bookmarks = [],
        categories = [],

    paginator = Paginator(bookmarks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/search.html', {'b': b, 'bookmarks': bookmarks, 'page_obj': page_obj, 'categories': categories, 'query': query})












