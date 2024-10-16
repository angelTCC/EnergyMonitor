from django.urls import path
from ProjectWebApp import views

urlpatterns = [
    path('', views.home, name='home')
]