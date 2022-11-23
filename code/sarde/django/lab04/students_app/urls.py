from django.urls import path
from . import views

app_name = 'students_app'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),

]
