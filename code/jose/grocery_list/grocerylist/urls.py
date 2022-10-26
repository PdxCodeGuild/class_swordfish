from django.urls import path, include
from ..Grocery_List import views

app_name='grocerylist'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path('add/', views.add, name='add'),
    path("complete/<int:pk>/", views.complete, name='completed'),
    path("delete/<int:pk>/", views.delete, name='delete')

    # path('grocery-list', views.Groceries, )
]
