from django.contrib import admin
from django.urls import path

from . import views

app_name = "url_shortener"

urlpatterns = [
    path("", views.index, name="index"),
    path("submit-url/", views.submit_url, name="submit_url"),
    path("redirect/<str:code>/", views.url_redirect, name="url_redirect"),
]