"""pokedex_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from apis.views import UserViewSet, PokemonViewSet, TypeViewSet, CurrentUserViewSet
from rest_framework import routers
# from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'pokemons', PokemonViewSet, basename='pokemons')
router.register(r'types', TypeViewSet, basename='types')
router.register(r'current-user', CurrentUserViewSet, basename='current-user')
# router.register('user', UserViewSet, basename='user')
# router.register('pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    # admin/doc/ needs to be above the line for our admin.site.urls
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/v1/', include(router.urls)),
    # this is specifically for django tool additions
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# api/v1/ is used for version tracking in case we change  api versions, we can still have a running previous version
