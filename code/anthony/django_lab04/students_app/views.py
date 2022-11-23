from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
def index(request):
    return HttpResponse("ok")


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer