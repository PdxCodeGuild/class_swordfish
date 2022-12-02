from django.urls import path
from . import views

app_name = 'Chirps'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.newchirp, name="newchirp" )
]
