from django.urls import path
from . import views
urlpatterns = [
    path('layouts/base/', views.layouts_base),
     path('users/SignUp/', views.user_register, name="user.SignUp"),
    path('users/LogIn/', views.user_login, name="user.LogIn"),
]