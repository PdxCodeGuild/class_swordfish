from msilib.schema import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url: reverse_lazy('chirp:home')

    def test_func(self):
        post = self.get_object
        return self.request.user == post.author

