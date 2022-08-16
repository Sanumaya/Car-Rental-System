from django.urls import path
from . import views
urlpatterns = [
    path('layouts/base/', views.layouts_base),
]