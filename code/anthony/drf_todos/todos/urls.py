from django.urls import path
from rest_framework import routers
# from .views import ListTodo, DetailTodo, index 
from .views import TodoViewSet


router = routers.DefaultRouter()

# http://localhost:8000/todos
router.register('', TodoViewSet)

urlpatterns = router.urls




# urlpatterns = [
#     # http://localhost:8000/todos
#     path("", ListTodo.as_view()),
#     # http://localhost:8000/todos/2
#     path("<int:pk>/", DetailTodo.as_view()),
#     path("home", index, name="index")
# ]
