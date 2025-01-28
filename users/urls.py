from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("register/", views.register, name="register"),
]