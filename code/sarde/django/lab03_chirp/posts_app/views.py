from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts_app/posts.html', {'posts': posts})

# LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts_app/new_post.html'
    fields = ['post_text']
    success_url = reverse_lazy('posts_app:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



