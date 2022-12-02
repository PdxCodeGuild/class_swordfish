from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'students'

router = DefaultRouter()
router.register('students', views.ListStudents)

urlpatterns = [
    path('/', views.index, name='index')
] + router.urls