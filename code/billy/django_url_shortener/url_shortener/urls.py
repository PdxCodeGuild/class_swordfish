from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.add_url, name = 'create'),
    path('<str:pk>', views.url_shortener, name = 'shorten')
]