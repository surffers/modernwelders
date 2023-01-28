from django.urls import path
from django.contrib.auth import views
from django.conf.urls import handler400, handler403, handler404, handler500
from apps.courses.views import courses
from . import views

urlpatterns = [
    #
    #
    path('courses/', courses, name='courses'),
]