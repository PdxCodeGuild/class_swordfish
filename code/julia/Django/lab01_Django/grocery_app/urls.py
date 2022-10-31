from django.urls import path
from . import views


app_name = "grocery_app"

urlpatterns = [
    path("", views.basis, name='basis')
    path("add/", views.add, name='add'),
    path("complete/<int:pk>/", views.complete, name='complete'),
    path("delete/<int:pk>/", views.delete, name='delete'),
]
     
 
 