from django.urls import path
from rest_framework import routers
from .views import PokemonViewSet

router = routers.DefaultRouter()

#http://localhost:8000/pokemon_api
router.register('', PokemonViewSet)

urlpatterns = router.urls
    

