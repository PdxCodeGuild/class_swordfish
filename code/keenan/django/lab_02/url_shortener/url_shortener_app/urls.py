from django.urls import path
from . import views

app_name = 'url_shortener_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('redirect-view/<str:short>/', views.redirect_view, name='redirect')
]