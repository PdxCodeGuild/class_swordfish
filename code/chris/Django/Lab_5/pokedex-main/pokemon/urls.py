from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "Pokemon"

router = DefaultRouter()
router.register("pokemon", views.PokemonViewSet)

urlpatterns = [
    path("", views.index, name="index")
] + router.urls
