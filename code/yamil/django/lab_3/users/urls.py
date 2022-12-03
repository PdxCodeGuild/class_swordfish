from django.urls import path
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.NewUser.as_view(), name='signup'),
    path('<str:username>/', views.user_profile, name='profile'),
]
