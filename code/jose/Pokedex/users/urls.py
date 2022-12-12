from django.urls import path, include
from . views import SignUpView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup')
]
