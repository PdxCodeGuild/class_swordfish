from django.shortcuts import render
from . models import Students
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, permissions
from . serializers import StudentsSerializer
# Create your views here.

def index(request):
    students = Students.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('Last_name')
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticated]
