from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# def mylogin(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     # if user is not None:
    #     login(request, user)
    #     # redirect to a success page
    # else:
    #     # return an 'invalid login' error message

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = User
    template_name='user_profile.html'
    context_object_name='user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

def user_profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {
        'user_profile' : user_profile
        }
    return render(request, 'user_profile.html', context)
