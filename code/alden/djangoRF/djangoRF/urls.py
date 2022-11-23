from django.urls import path
from .views import StudentViewSet
from rest_framework import routers

app_name = 'djangoRF' # for namespacing
router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='students')
urlpatterns = router.urls