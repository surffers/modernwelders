"""surffers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from apps.bookmark.views import category, category_edit, category_delete, bookmark_add, bookmark_delete, bookmark_edit, \
    tag_detail, drafts, category_publish, bookmark_detail, favorite_bookmark, bookmark_publish, sponsors, vote


urlpatterns = [
    #
    #
    path('category/<str:slug>-<int:category_id>/', category, name='category'),
    path('category/<str:slug>-<int:category_id>/publish/', category_publish, name='category_publish'),
    path('category/<str:slug>-<int:category_id>/edit/', category_edit, name='category_edit'),
    path('category/<str:slug>-<int:category_id>/delete/', category_delete, name='category_delete'),
    path('category/<str:slug>-<int:category_id>/add_bookmark/', bookmark_add, name='bookmark_add'),

    path('delete_bookmark/<int:bookmark_id>/', bookmark_delete, name='bookmark_delete'),
    path('bookmark_edit/<int:bookmark_id>/', bookmark_edit, name='bookmark_edit'),

    path('<int:bookmark_id>/', favorite_bookmark, name='favorite_bookmark'),
    path('b/<int:bookmark_id>/vote/', vote, name='vote'),

    path('drafts/', drafts, name='drafts'),
    path('sponsors/', sponsors, name='sponsors'),

    # path('create/', create, name='create'),
    # Tags
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    # Comment
    path('link/<int:bookmark_id>/', bookmark_detail, name='bookmark'),
    path('link/<int:bookmark_id>/publish/', bookmark_publish, name='bookmark_publish'),
]
