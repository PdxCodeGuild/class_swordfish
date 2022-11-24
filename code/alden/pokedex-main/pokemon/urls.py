from django.urls import path
from .views import PokemonViewSet
from rest_framework import routers

app_name = 'pokemon'

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('/', PokemonViewSet, name='index')
] + router.urls