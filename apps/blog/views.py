from django.shortcuts import render


def blog(request):
    context = {

    }
    return render(request, 'blog/blog.html', context)


def about(request):
    context = {

    }
    return render(request, 'blog/about.html', context)