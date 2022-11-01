from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('join/', views.UserCreateView.as_view(), name='join'),
    path('<str:user>/', views.UserProfileView.as_view(), name='profile')
]