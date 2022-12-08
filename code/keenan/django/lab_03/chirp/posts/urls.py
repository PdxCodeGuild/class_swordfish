from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('new', views.ChirpCreateView.as_view(), name='new'),
]
