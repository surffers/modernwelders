from django.urls import path
from django.contrib.auth import views

from django.conf.urls import handler400, handler403, handler404, handler500


from apps.userprofiles.views import profile, edit_profile, link_delete, bookmark_favorite_lists, user_links, follow_user, unfollow_user, followers, follows


urlpatterns = [
    #
    #
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/followers/', followers, name='followers'),
    path('<str:username>/follows/', follows, name='follows'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),
    path('<link_id>/delete/', link_delete, name='link_delete'),
    path('<str:username>/favorite/', bookmark_favorite_lists, name='bookmark_favorite_lists'),
    path('<str:username>/links/', user_links, name='user_links')

] 