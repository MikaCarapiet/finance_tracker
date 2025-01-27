from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
]