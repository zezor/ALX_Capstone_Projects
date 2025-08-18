
from django import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pfm.urls')),
    path('', include('accounts.urls')),
    path('', views.home, name='home'),
]
