from django.urls import path 
from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.add, name='add'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]