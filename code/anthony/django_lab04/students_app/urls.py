from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "students_app"

router = DefaultRouter()
router.register("/students", views.StudentViewSet, basename="students")

# localhost:8000/api/
urlpatterns = [
    path("/", views.index, name="index")
] + router.urls
