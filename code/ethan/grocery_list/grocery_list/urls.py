from django.urls import path
from . import views


app_name = 'grocery_list' # for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:item_id>', views.complete, name = 'complete'),
    path('delete/<int:item_id>', views.delete, name = 'delete'),
]