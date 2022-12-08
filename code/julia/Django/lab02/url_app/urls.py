from django.urls import path
from . import views



app_name = 'url_app'

urlpatterns=[
    path('', views.index, name='index'),
    path('url_app/<str:short_url>/',views.redirect, name='redirect' ),
    
    
]