from django.urls import path, include
from django.contrib import admin
from . import views
app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('<str:username>/', views.UserProfileView.as_view(), name="profile")
]
