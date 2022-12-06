from django.urls import path

from .views import ListPokemon, DetailPokemon, ListType

urlpatterns = [
    path('pokemon/', ListPokemon.as_view()),
    path('type', ListType.as_view()),
    path('pokemon/<int:pk>/', DetailPokemon.as_view())
]
