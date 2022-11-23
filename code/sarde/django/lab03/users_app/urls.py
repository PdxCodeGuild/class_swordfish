from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('signup/', views.signup, name='signup'),
    path('render-signup/', views.render_signup, name='render_signup'),
    path('render-login/', views.render_login, name='render_login'),
    path('login/', views.login, name='login')
]
