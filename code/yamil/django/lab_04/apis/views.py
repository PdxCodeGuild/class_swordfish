from rest_framework import viewsets

from students import models
from .serializers import StudentsSerializer

# class ListStudents(generics.ListCreateAPIView):
#     queryset = models.Students.objects.all()
#     serializer_class = StudentsSerializer

# class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Students.objects.all()
#     serializer_class = StudentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = StudentsSerializer