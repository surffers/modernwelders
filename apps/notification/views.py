from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Notification
from apps.bookmark.models import Bookmark


@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('conversation', user_id=notification.created_by.id)
        elif notification.notification_type == Notification.FOLLOWER:
            return redirect('profile', username=notification.created_by.username)
        elif notification.notification_type == Notification.VOTE:
            return redirect('profile', username=notification.created_by.username)
        elif notification.notification_type == Notification.MENTION:
            return redirect('profile', username=notification.created_by.username)

    return render(request, 'notification/notifications.html')