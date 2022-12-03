from django.urls import path
from . import views
from .views import SignUpView


app_name = 'users'

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('login', views.login, name='login')
   

]

