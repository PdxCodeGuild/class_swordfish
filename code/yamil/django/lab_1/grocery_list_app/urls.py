from django.urls import path
from . import views

urlpatterns = [
    path('grocery_list/', views.say_hello)
]