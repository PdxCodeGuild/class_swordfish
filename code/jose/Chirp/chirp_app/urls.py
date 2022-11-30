from django.urls import path
from . import views


app_name = 'chirp_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.new_post, name='add')

]