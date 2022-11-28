from django.urls import path
from .views import PokemonViewSet, profileview, caughtPokemon, releasedPokemon
from rest_framework import routers

app_name = 'pokemon'

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('profile/', profileview, name='index'),
    path('caught/<int:pokemon_id>', caughtPokemon, name='caught'),
    path('release/<int:pokemon_id>', releasedPokemon, name='release')
] + router.urls