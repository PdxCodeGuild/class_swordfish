from django.urls import path
from .views import ListTodo, DetailTodo, index

urlpatterns = [
    # http://localhost:8000/todos
    path("", ListTodo.as_view()),
    # http://localhost:8000/todos/2
    path("<int:pk>/", DetailTodo.as_view()),
    path("home", index, name="index")
]
