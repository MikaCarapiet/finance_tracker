from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # ex: /polls/
    path("register/", views.register, name="register"),
]