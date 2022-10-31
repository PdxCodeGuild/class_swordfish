from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('posts:home')

def profile(request, username):
    profile = get_object_or_404(User, username=username)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)