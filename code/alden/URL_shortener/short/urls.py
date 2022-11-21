from django.urls import path
from . import views

app_name = 'short' # for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('short/submit/', views.submit, name='submit'),
    path('<str:code>/', views.code, name='code'),
]