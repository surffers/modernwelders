from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #
    # Admin
    path('admin/', admin.site.urls),#hc81inkjyp1h&wgk3s83
    #
    # Accounts
    path('accounts/', include('allauth.urls')),
    #
    # Core
    path('', include('apps.core.urls')),
    # Document
    path('', include('apps.document.urls')),
    #
    # Feed
    path('', include('apps.bookmark.urls')),
    # Blog
    path('', include('apps.blog.urls')),
    # Contact
    path('contact/', include('apps.contact.urls')),
    #
    # Profiles
    path('', include('apps.userprofiles.urls')),



] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.core.views.error_404_view'