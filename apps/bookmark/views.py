from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
import datetime

from django.utils import timezone

from .models import Category, Bookmark, Comment
from apps.userprofiles.models import Profile
from .forms import CategoryForm, BookmarkForm, CommentForm
from taggit.models import Tag
from django.urls import reverse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    is_favorite = False
    if bookmark.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    if request.method == 'POST' and 'btnedit' in request.POST:
        BookmarkEdit = BookmarkForm(request.POST, request.FILES, instance=bookmark)

        if BookmarkEdit.is_valid():
            BookmarkEdit.save()

            return redirect('bookmark', bookmark_id=bookmark_id)
    else:
        BookmarkEdit = BookmarkForm(instance=bookmark)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.bookmark_id = bookmark_id

            comment.save()

            return redirect('bookmark', bookmark_id=bookmark_id)
    else:
        form = CommentForm()



    context = {
        'bookmark': bookmark,
        'form': form,
        'is_favorite': is_favorite,
        'BookmarkEdit': BookmarkEdit,
    }

    return render(request, 'feed/bookmark_detail.html', context)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    # tag = get_object_or_404(Tag, slug__iexact=slug)
    bookmarks = Bookmark.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'bookmarks': bookmarks,
    }
    return render(request, 'feed/tags.html', context)


def category(request, category_id):

    category = Category.objects.get(pk=category_id)
    bookmarks = Bookmark.objects.filter(category_id=category_id)
    b = Bookmark.objects.all()

    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.category_id = category_id
            bookmark.save()
            messages.success(request, 'Ссылка добавлена!')
            form.save_m2m()
            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm()

    if request.method == 'POST' and 'btnedit' in request.POST:
        FormEdit = CategoryForm(request.POST, request.FILES, instance=category)
        if FormEdit.is_valid():
            FormEdit.save()
            messages.success(request, 'Изменения сохранены!')
            return redirect('category', category_id=category_id)
    else:
        FormEdit = CategoryForm()

    if request.method == 'POST' and 'btnaddcategory' in request.POST:
        AddCategoryForm = CategoryForm(request.POST, request.FILES)
        if AddCategoryForm.is_valid():
            category = AddCategoryForm.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Категория созданна!')
            return redirect('category', category_id=category_id)
    else:
        AddCategoryForm = CategoryForm()

    context = {
        'bookmarks': bookmarks,
        'category': category,
        'form': form,
        'FormEdit': FormEdit,
        'AddCategoryForm': AddCategoryForm,
        'b': b,
    }

    return render(request, 'feed/category.html', context)


@login_required
def category_add(request, category_id):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()

            messages.success(request, 'Категория создана!')

            return redirect('category', category_id=category_id)
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }

    return render(request, 'feed/category_add.html', context)


@login_required
def category_publish(request, category_id):
    cat = get_object_or_404(Category, id=category_id)
    cat.publish()
    return redirect('category', category_id=category_id)


@login_required
def category_edit(request, category_id):
    category = Category.objects.filter(user=request.user).get(pk=category_id)

    if request.method == 'POST':
        FormEdit = CategoryForm(request.POST, request.FILES, instance=category)
        if FormEdit.is_valid():
            FormEdit.save()
            messages.success(request, 'Изменения сохранены!')
            return redirect('category', category_id=category_id)
    else:
        FormEdit = CategoryForm(instance=category)

    context = {
        'category': category,
        'FormEdit': FormEdit,
    }

    return render(request, 'feed/include/category_edit.html', context)


@login_required
def category_delete(request, category_id):
    category = Category.objects.filter(user=request.user).get(id=category_id)
    category.delete(request.POST, request.FILES)
    messages.success(request, 'Категория удалена!')
    return redirect('profile', username=request.user.username)


@login_required
def bookmark_add(request, category_id):
    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.category_id = category_id
            bookmark.save()
            messages.success(request, 'Ссылка добавлена!')
            form.save_m2m()
            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm()

    context = {
        'form': form,
    }

    return render(request, 'feed/add_bookmark.html', context)


@login_required
def bookmark_publish(request, bookmark_id):
    book = get_object_or_404(Bookmark, id=bookmark_id)
    book.publish()
    return redirect('bookmark', bookmark_id=bookmark_id)


@login_required
def bookmark_edit(request, bookmark_id):
    bookmark = Bookmark.objects.filter(user=request.user).get(pk=bookmark_id)

    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES, instance=bookmark)

        if form.is_valid():
            form.save()

            return redirect('bookmark', bookmark_id=bookmark_id)
    else:
        form = BookmarkForm(instance=bookmark)

    context = {
        'form': form,
        'bookmark': bookmark
    }

    return render(request, 'feed/include/bookmark_edit.html', context)


@login_required
def bookmark_delete(request, bookmark_id):
    bookmark = Bookmark.objects.filter(user=request.user).get(pk=bookmark_id)
    bookmark.delete(request.POST, request.FILES)
    messages.success(request, 'Ссылка удалена!')
    return redirect('board')


@login_required
def favorite_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)

    if bookmark.favorite.filter(id=request.user.id).exists():
        bookmark.favorite.remove(request.user)
        messages.success(request, 'Ссылка удалена из избранного!')
    else:
        bookmark.favorite.add(request.user)
        messages.success(request, 'Ссылка добавлена из избранное!')
    return redirect('bookmark', bookmark_id=bookmark_id)


@login_required
def drafts(request):
    userids = [request.user.id]

    categories_drafts = Category.objects.filter(user_id__in=userids, published_date__isnull=True).order_by('-created_at')
    user_bookmarks = Bookmark.objects.all().select_related('user', 'category', ).order_by("-created_at")

    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.category_id = bookmark.category_id
            bookmark.save()
            return redirect('drafts')
    else:
        form = BookmarkForm()

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('drafts')

    paginator = Paginator(categories_drafts, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj,
        'user_bookmarks': user_bookmarks,
        'categories_drafts': categories_drafts,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/draft_lists.html', context)
