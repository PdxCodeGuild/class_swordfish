from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Posts

def index(request):
    list_of_posts = Posts.objects.all().order_by('-created_date')
    context = {
        'list_of_posts' : list_of_posts
    }
    return render(request, 'homepage.html', context)

def add(request):
    if request.user.is_authenticated == True:
        new_post_body = request.POST['post_body']
        Posts.objects.create(post_body=new_post_body,post_author=request.user)
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        return HttpResponseRedirect(reverse('login'))