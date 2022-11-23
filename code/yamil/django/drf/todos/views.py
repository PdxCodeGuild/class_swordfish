from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# class ListTodo(generics.ListCreateAPIView):
#     todos = Todo.objects.all()
#     queryset = todos
#     serializer_class = TodoSerializer

# class DetailTodo(generics.RetrieveDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
    
# def index(request):
#     return render(request, "todos/index.html")