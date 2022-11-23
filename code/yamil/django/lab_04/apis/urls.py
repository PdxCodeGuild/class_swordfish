from django.urls import path

from .views import StudentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentsViewSet, basename='todos')
urlpatterns = router.urls