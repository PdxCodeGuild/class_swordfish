from django.urls import path
from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('hello-world/', views.hello_world, name='helloworld'),
    path('', views.index, name='grocerylist')
]
# http://localhost:8000/grocery-list/hello-world/
# http://localhost:8000/grocery-list/