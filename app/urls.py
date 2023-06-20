from django.contrib import admin
from django.urls import path
from app import views




urlpatterns = [
    path('', views.index),
    path('registration/', views.Registration),
    path('courses/', views.Courses),
]
