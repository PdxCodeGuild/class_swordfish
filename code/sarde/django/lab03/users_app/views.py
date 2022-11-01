from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)


def signup(request):
    the_username = request.POST.get('username')
    user_email = request.POST.get('email')
    user_password = request.POST.get('password')
    # print(the_username, user_email, user_password)
    users = User.objects.all()
    print('Users', users)
    for user in users:
        if user.username == the_username:
            print('user.username', user.username)
            print('the_username', the_username)
            print('Cannot create user, user already exists')
            return HttpResponseRedirect(reverse('users_app:render_signup'))

    print('user.username', user.username)
    print('the_username', the_username)
    print('User can be created')
    user = User.objects.create_user(
        the_username, user_email, user_password)
    return HttpResponseRedirect(reverse('users_app:render_login'))


def render_signup(request):
    return render(request, 'users_app/signup.html')


def login(request):
    login_username = request.POST['username']
    login_password = request.POST['password']
    logged_user = authenticate(request, username=login_username,
                               password=login_password)
    if user is not None:
        login(request, logged_user)
    else:
        return f'invalid login'


def render_login(request):
    return render(request, 'users_app/login.html')

    # def user_profile(request):
