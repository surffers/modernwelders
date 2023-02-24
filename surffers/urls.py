from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
import debug_toolbar
from apps.notification.views import notifications
from django.conf import settings
from django.conf.urls.static import static

from apps.bookmark.sitemap import CategorySitemap, BookmarkSitemap
from apps.core.sitemap import StaticSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView


sitemaps = {
    'categories': CategorySitemap,
    'bookmarks': BookmarkSitemap,
    'static': StaticSitemap,
    }


urlpatterns = [
    #
    # Admin
    path('hc81inkjy/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('hc81inkjyp1h&wgk3s83/', admin.site.urls),#hc81inkjyp1h&wgk3s83

    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #
    # Accounts
    path('accounts/', include('allauth.urls')),
    #
    # Notifications
    path('notifications/', notifications, name='notifications'),
    #
    # Core
    path('', include('apps.core.urls')),
    # Document
    path('', include('apps.document.urls')),
    #
    # Feed
    path('', include('apps.bookmark.urls')),
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