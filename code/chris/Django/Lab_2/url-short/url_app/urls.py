from django.urls import path

from . import views
#import 3rd party libraries first then package

app_name = 'url_app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('url_final/<int:pk>/', 'url_final', views.url_final, name='final'),
    # path('redirect/<int:pk>/', 'redirect', views.redirect, name='redirect'),
]