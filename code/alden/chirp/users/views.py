from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

def user_profile(request, username):
    user_profile = get_object_or_404(User, username = username)
    context = {'user_profile': user_profile}
    return render(request, 'user_profile.html', context)
