from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')

app_name = 'students_app'

urlpatterns = [
    path('', views.index, name='index'),
] + router.urls

