from django.urls import path
from .views import StudentList

urlpatterns = [
    path("", StudentList.as_view())
]
