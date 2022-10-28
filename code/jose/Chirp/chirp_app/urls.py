from django.urls import path
from . import views

app_name = 'chirp_app' # for namespacing
urlpatterns = [
    # path('index', views.index, name='index'),
    path('home/', views.ChirpListView.as_view())

]