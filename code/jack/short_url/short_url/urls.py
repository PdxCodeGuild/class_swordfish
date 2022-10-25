from django.urls import path
from . import views

app_name = 'short_url'
urlpatterns = [
    path('/', views.index, name='index'),
    path('/create/', views.create, name='create'),
    path('/<str:code>/', views.redirect, name='redirect'),
]