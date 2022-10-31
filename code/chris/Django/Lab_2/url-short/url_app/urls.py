from django.urls import path

from . import views
#import 3rd party libraries first then package

app_name = 'url_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('shortcode/', views.shortcode, name='shortcode'),
    path('redirect/<str:code>/', views.redirect, name='redirect'),
]