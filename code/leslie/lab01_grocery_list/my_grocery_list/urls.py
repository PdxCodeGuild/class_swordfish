from django.contrib import admin
from django.urls import path
from . import views


app_name = 'my_grocery_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_list, name='list_view'),
    path('add/', views.add, name='add'),
    path('complete/<int:item_id>/', views.complete, name='complete'),
    path('delete/<int:item_id>/', views.delete, name='delete')

]
