from django.urls import path
from . import views


app_name = 'url_app'

urlpatters=[
    path('', views.index, name='index')
    
]