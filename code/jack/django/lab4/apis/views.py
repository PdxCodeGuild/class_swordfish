from django.shortcuts import render
from rest_framework import generics
from students_app import models
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer