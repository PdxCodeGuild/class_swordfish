from .import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')

app_name = 'pokemon'

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/new/', views.PokemonCreateView.as_view(), name='new_pokemon'),
    path('pokemon/edit/<int:pokemon_id>', views.edit, name='edit_pokemon'),
] + router.urls

