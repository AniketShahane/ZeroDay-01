from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('donors/', views.donors, name='donors'),
    path('children/', views.children, name='children')
]
