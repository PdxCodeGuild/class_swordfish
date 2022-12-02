from django.urls import path
from . import views

app_name = 'urlshortener' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('returnshorturl', views.returnshorturl, name='returnshorturl' )
]