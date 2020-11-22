from django.contrib import admin
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('', views.index),
    path('register/', views.registerUser),
    path('logout', views.logoutUser),
    path('login', views.loginUser),
   
]