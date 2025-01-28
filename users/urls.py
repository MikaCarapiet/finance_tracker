from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # ex: /polls/
    path("register/", views.register, name="register"),
]