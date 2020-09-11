# from django.contrib import admin
from django.urls import path, include
from usersApp import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    # path('admin/', admin.site.urls),
]
