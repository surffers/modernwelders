from django.shortcuts import render, redirect, get_object_or_404


def privacy(request):

    context = {

    }
    return render(request, 'document/privacy.html', context)
