from django.urls import path
from django.contrib import admin
from . import views

app_name = 'finance_tracker'

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
]