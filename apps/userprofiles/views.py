from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Profile, Link
from apps.bookmark.models import Category, Bookmark
from .forms import ProfileForm, LinkForm
from apps.bookmark.forms import CategoryForm


@login_required
def user_links(request, username):
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
    return render(request, 'profiles/user_links.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    links = Link.objects.filter(user=user)
    bookmarks = Bookmark.objects.filter(user=user).select_related('category', 'user')
    categories = Category.objects.filter(user=user, published_date__lte=timezone.now()).order_by("created_at")
    categories_public = Category.objects.filter(user=user).select_related('user')
    categories_drafts = Category.objects.filter(user=user, published_date__isnull=True)
    favorite_bookmarks = user.favorite.all()

    # Add link
    if request.method == 'POST' and 'btnlink' in request.POST:
        AddLinkForm = LinkForm(request.POST)
        if AddLinkForm.is_valid():
            link = AddLinkForm.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('profile', username=request.user.username)
    else:
        AddLinkForm = LinkForm()

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category', category_id=category.id)

    if request.method == 'POST':
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            messages.success(request, 'Изменения сохранены!')
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=user.profile)

    paginator = Paginator(categories, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': user,
        'page_obj': page_obj,
        'links': links,
        'bookmarks': bookmarks,
        'categories': categories,
        'categories_drafts': categories_drafts,
        'categories_public': categories_public,
        'AddLinkForm': AddLinkForm,
        'UserEditForm': UserEditForm,
        'AddCategoryForm': AddCategoryForm,
        'favorite_bookmarks': favorite_bookmarks,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def link_add(request):
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('profile', username=request.user.username)
    else:
        form = LinkForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/add_link.html', context)


@login_required
def link_delete(request, link_id):
    link = Link.objects.get(pk=link_id)
    link.delete()
    return redirect('profile', username=request.user.username)





@login_required
def edit_profile(request):
    if request.method == 'POST':
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            messages.success(request, 'Изменения сохранены!')
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=request.user.profile)

    context = {
        'UserEditForm': UserEditForm
    }

    return render(request, 'profiles/edit_profile.html', context)


@login_required
def bookmark_favorite_lists(request, username):
    user = request.user
    favorite_bookmarks = user.favorite.all()
    links = Link.objects.filter(user=user)
    bookmarks = Bookmark.objects.all().select_related('category')
    categories = Category.objects.filter(user=user).order_by("created_at")

    context = {
        'favorite_bookmarks': favorite_bookmarks,
        'links': links,
        'bookmarks': bookmarks,
        'categories': categories,
    }
    return render(request, 'profiles/favorite_profile.html', context)