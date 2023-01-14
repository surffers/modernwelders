from django.urls import path
from apps.blog.views import blog, about


urlpatterns = [
    #
    #
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
]