from django.urls import path
from . import views

app_name = 'posts_app'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('', views.index, name='index'),
    path('new/', views.PostCreateView.as_view(), name='new'),
]
