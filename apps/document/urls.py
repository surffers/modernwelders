from django.urls import path
from django.contrib.auth import views
from django.conf.urls import handler400, handler403, handler404, handler500
from apps.document.views import privacy
from . import views

urlpatterns = [
    #
    #
    path('privacy/', privacy, name='privacy'),
]