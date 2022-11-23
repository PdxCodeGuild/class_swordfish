from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'studentsapp' # for namespacing
router = DefaultRouter()
router.register("students/", views.StudentViewSet)
urlpatterns = [
    path('', views.index, name='index')
] + router.urls

urlpatterns = router.urls