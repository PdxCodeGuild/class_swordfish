URLfrom django.urls import path

from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/incomplete/', views.incomplete, name='incomplete'),
    path('<int:item_id>/complete/', views.complete, name='complete'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<add/', views.add, name='add')
]
