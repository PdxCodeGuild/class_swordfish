
from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create, name='create'),
    path('post/<int:post_pk>/', views.detail, name='detail'),
    path('post/<int:post_pk>/edit/', views.edit, name='edit'),
    path('post/<int:post_pk>/delete/', views.delete, name='delete'),
    path('forbidden/', views.forbidden, name='forbidden'),
]
