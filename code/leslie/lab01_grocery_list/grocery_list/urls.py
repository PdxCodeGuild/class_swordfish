from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_list/', include('my_grocery_list.urls'))
]
