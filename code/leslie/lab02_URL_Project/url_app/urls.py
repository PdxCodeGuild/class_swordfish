from django.urls import path
from . import views

app_name = "url_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('shorten_url', views.shorten_url, name='shorten_url'),
    

]