from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import CustomUser
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])