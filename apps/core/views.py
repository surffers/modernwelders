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
from django.contrib import messages


@login_required
def users_links_lists(request):
    all_categories = Category.objects.all().select_related('user')
    userids = [request.user.id]
    bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('category')
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
    categories = Category.objects.all()#[0:3]

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
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    tags = Tag.objects.all
    # userids = [request.user.id]

    profiles = Profile.objects.all().order_by("-created")
    home_categories = Category.objects.filter(published_date__lte=timezone.now()).order_by("-created_at")#[0:3]
    bookmarks = Bookmark.objects.filter(published_date__lte=timezone.now())
    user_categories = Category.objects.filter(published_date__lte=timezone.now())


    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        messages.success(request, 'Категория создана!')
        return redirect('categories')


    paginator = Paginator(bookmarks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
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
    all_categories = Category.objects.filter(published_date__lte=timezone.now()).select_related()
    categories = Category.objects.all()
    bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('category')

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
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/dashboard.html', context)


def search(request):
    home_categories = Category.objects.filter(published_date__lte=timezone.now())
    query = request.GET.get('query', '')

    if len(query) > 0:
        bookmarks = Bookmark.objects.filter(title__icontains=query, published_date__lte=timezone.now())
        categories = Category.objects.filter(title__icontains=query, published_date__lte=timezone.now())

    else:
        bookmarks = [],
        categories = []

    paginator = Paginator(bookmarks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/search.html', {'home_categories': home_categories, 'bookmarks': bookmarks, 'page_obj': page_obj, 'categories': categories, 'query': query})












