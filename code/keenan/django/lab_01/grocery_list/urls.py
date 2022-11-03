from django.urls import path
from . import views

app_name = 'grocery_list' 

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('complete/<int:pk>', views.complete, name='complete' )
]