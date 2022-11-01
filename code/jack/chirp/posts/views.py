from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post


def home(request):
    posts = Post.objects.all()[:10]
    context = {'posts': posts}
    return render(request, 'home.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        post = Post(title=title, body=body, author=request.user)
        post.save()

        posts = Post.objects.all()[:10]
        context = {'posts': posts}
        return render(request, 'home.html', context)
    else:
        return render(request, 'post_create.html')


def detail(request, post_pk):
    post = get_object_or_404(Post.objects.filter(pk=post_pk))
    context = {'post':post}
    return render(request, 'post_detail.html', context)


def edit(request, post_pk):
    post = get_object_or_404(Post.objects.filter(pk=post_pk))
    if request.user == post.author:
        if request.method == 'POST':
            post.title = request.POST['title']
            post.body = request.POST['body']
            post.save()

            posts = Post.objects.all()[:10]
            context = {'posts': posts}
            return HttpResponseRedirect(reverse('posts:home'))
        context = {'post':post}
        return render(request, 'post_edit.html', context)
    else:
        return HttpResponseRedirect(reverse('posts:forbidden'))


def delete(request, post_pk):
    post = get_object_or_404(Post.objects.filter(pk=post_pk))
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return HttpResponseRedirect(reverse('posts:home'))
        else:
            context = {'post':post}
            return render(request, 'post_delete.html', context)
    else:
        return HttpResponseRedirect(reverse('posts:forbidden'))
    
def forbidden(request):
    return render(request, 'forbidden.html')
