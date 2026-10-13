from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('registro/', views.SignupView.as_view(), name='signup'),
    path('entrar/', views.LoginView.as_view(), name='login'),
    path('salir/', LogoutView.as_view(), name='logout'),
]
