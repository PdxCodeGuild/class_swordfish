from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
]
