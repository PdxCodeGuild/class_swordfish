from django.urls import path
from . import views
from users.views import chirperprofile
app_name = 'Chirps'

urlpatterns = [
    path('', views.index, name='index'),
    path('newchirp/', views.newchirp, name="newchirp" ),
    path('chirperprofile', chirperprofile, name='chirperprofile')
    # path('chirp_list/', )
]
