from django.urls import path
from . import views

app_name = 'users' # for namespacing
urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
]