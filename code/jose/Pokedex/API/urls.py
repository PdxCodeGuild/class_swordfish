from django.urls import path, revers, reverse_lazy
from . views import ListPokemon, ListType, DetailPokemon

urlpatterns = [
    path('pokemon/', ListPokemon.as_view()),
    path('type/', ListType.as_view()),
    path('pokemon/<int:pk>/', DetailPokemon.as_view())
]
