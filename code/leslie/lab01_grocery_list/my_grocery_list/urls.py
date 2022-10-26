from django.contrib import admin
from django.urls import path
from . import views


app_name = 'my_grocery_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
