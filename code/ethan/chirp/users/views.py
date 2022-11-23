from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class CreateUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('login')