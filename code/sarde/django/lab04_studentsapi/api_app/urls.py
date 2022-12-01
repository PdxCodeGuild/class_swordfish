from django.urls import path
from rest_framework import routers
from .views import StudentViewSet

router = routers.DefaultRouter()

router.register('', StudentViewSet)

urlpatterns = router.urls


