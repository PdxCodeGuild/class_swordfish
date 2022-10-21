from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:grocery_item>/form', views.form, name='form'),
    path('<str:grocery_item>/complete/', views.complete, name='complete'),
    path('<str:grocery_item>/delete/', views.delete, name='delete'),
]