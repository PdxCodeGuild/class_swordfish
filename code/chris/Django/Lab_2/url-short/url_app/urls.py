from django.urls import path

from . import views
#import 3rd party libraries first then package

urlpatterns = [
    path('', views.index, name='index'),
]