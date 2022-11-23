from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import StudentList
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentList.objects.all()
    serializer_class = StudentSerializer