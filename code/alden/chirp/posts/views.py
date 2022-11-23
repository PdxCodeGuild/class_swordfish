
from django.views.generic import ListView
from time import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .models import Posts

# class PostListView(ListView):
#     model = Posts
#     template_name = 'index.html'

def index(request):
    posts = Posts.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, 'index.html', context)

def new_post(request):
    if request.user.is_authenticated == True:
        posts = request.POST['post']
        Posts.objects.create(post = posts, author = request.user)
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        return HttpResponseRedirect(reverse('login'))
    