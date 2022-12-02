from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Posts

def index(request):
    list_of_posts = Posts.objects.all()
    context = {
        'the_stuff' : list_of_posts
    }
    return render(request, 'index.html', context)

def add(request):
    new_post_title = request.POST['post_title']
    new_post_body = request.POST['post_body']
    new_post = Posts.objects.create(post_body=new_post_body,post_title=new_post_title)
    return HttpResponseRedirect(reverse('posts:index'))