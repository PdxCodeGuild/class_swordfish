# from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from .forms import CustomUserCreationForm
from . models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(DetailView):
    model = CustomUser
    template_name = "profile.html"

