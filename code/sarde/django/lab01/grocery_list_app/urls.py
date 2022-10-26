from django.urls import path
from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('hello-world/', views.hello_world, name='helloworld'),
    path('', views.grocery_list, name='grocerylist'),
    path('add', views.add, name='add'),
    path('<int:item_id>/complete/', views.complete, name='complete'),
    path('<int:item_id>/incomplete/', views.incomplete, name='incomplete'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
   
]
# http://localhost:8000/grocery-list/hello-world/
# http://localhost:8000/grocery-list/

 #http://localhost:8000/grocery-list/7/complete/