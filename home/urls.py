from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('project/', views.project, name='project'),
    ]
