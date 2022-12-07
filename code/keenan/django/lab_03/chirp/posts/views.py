
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Post


class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'


class ChirpCreateView(CreateView):
    model = Post
    template_name = 'new_chirp.html'
    fields = ['title', 'post_body']
    # can pull the author if we can assign with username
    # posts: searches for a urls.py file with an app_name of 'posts' for the 'home' name
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
