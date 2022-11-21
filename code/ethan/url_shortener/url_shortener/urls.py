from django.urls import path
from . import views

app_name = 'url_shortener' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add-url', views.addurl, name='addurl'),
    path('<str:url_code>', views.redirect, name='redirect')

]