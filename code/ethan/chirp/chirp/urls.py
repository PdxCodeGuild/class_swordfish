from django.urls import path
from . import views

app_name = 'chirp' # for namespacing
urlpatterns = [
    path('', views.ChirpListView.as_view(), name='index'),
    path('chirp/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('chirp/new/', views.ChirpCreateView.as_view(), name='new_post'),
    path('chirp/<int:pk>/edit/', views.ChirpEditView.as_view(), name ='edit_post')
]