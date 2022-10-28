from venv import create
from django.urls import path
from . import views

app_name = 'url_shortener_app'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('short/<str:short_code>/', views.redirect, name='redirect'),
]
# localhost:8000/url-shortener/short/jymoDQ/
