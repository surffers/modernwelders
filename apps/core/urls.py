from django.urls import path
from django.contrib.auth import views
from django.conf.urls import handler400, handler403, handler404, handler500
from apps.core.views import search, home, categories, price, tests, users_links_lists
from . import views

urlpatterns = [
    #
    #
    path('', home, name='home'),
    path('links/', users_links_lists, name='board'),

    path('categories/', categories, name='categories'),
    path('search/', search, name='search'),
    path('price/', price, name='price'),
    path('tests/', tests, name='tests'),
]

