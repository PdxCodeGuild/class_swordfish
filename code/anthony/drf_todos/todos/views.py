from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    # queryset => specifies which data to return
    queryset = Todo.objects.all()
    # serializer_class => specifies which serializer to use
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer





# For display only, not required for DRF
def index(request):
    return render(request, "todos/index.html")