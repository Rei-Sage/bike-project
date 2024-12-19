from django.shortcuts import redirect
from django.urls import path, include
from .views import *
urlpatterns = [
    path('product/<int:id>/', detail, name='detail'),
    path('main',main,name='main'),
    path('<int:id>/', home, name='home'),
]

