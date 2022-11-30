from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_url/", views.submit_url, name="submit_url"),
    path("", views.url_redirect, name="url_redirect"),
]