from django.urls import path
from . import views

app_name = "chirps"

urlpatterns = [
    path('list/', views.ChirpListView.as_view(), name='list'),
    path('<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('new/', views.ChirpCreateView.as_view(), name='new'),

]


