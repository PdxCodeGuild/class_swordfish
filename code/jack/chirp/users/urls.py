from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('<str:username>/', views.profile, name='profile'),
]