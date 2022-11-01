from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts_app/posts.html', {'posts': posts})
