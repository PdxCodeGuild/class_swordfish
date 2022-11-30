from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


def index(request):
    # return HttpResponse('django connected')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
