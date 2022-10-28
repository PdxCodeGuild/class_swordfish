from django.urls import path
from . import views

app_name = 'chirp' # for namespacing
urlpatterns = [
    path('', views.BlogListView.as_view, name='index'),
]