from django.urls import path
from . import views


app_name = 'chirp_app' # for namespacing
urlpatterns = [
    # path('index', views.index, name='index'),
    path('chirp/', views.ChirpListView.as_view(), name='chirp'),
    path('chirp_app/', views.ChirpCreateView.as_view(), name='new'),
    path('chirp/<int:pk>/edit/', views.ChirpEditView.as_view(), name='edit'),
    path('chirp/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),

]