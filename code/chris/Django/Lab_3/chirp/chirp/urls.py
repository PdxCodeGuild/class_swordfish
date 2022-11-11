from django.urls import path

from . import views

app_name = "chirp"

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('create/', views.ChirpCreateView.as_view(), name='create'),
]