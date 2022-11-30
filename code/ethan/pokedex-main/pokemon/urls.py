from .import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokedex_project', views.PokemonViewSet, basename='pokedex_project')

app_name = 'pokemon'

urlpatterns = [
    path('/', views.index, name='index'),
] + router.urls

