from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
]
