from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    students = Student.objects.all()
    queryset = students #I MUST HAVE queryset for LISTCREATEView
    serializer_class = StudentSerializer #I MUST ALSO HAVE serializer_class for LISTCREATEView

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer