from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.PostListView.as_view(), name='index')
    path('add/', views.new_post, name='add')
]
