from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializers import StudentSerializer

class ListStudents(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

def index(request):
    return render(request, 'students/index.html')