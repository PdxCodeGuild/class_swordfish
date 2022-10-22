from django.urls import path
from . import views


app_name = 'grocery_list' # for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path("complete/<item_id>", views.completeItem, name = "complete"),
    path('deleteItem/<int:item_id>', views.deleteItem, name = "deleteitem"),
]