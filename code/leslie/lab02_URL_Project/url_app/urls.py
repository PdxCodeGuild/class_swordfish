from django.urls import path
from . import views

app_name = "url_app"

urlpatterns = [
    path('', views.index, name="index"),
    # path('long_url/<str:pk>/', views.long_url, name="long_url")

]