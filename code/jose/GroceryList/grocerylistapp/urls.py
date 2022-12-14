from django.urls import path
from . import views

app_name = 'grocerylistapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('completed/<int:pk>/', views.complete, name='complete'),
    path('incomplete/<int:pk>/', views.incomplete, name='incomplete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
