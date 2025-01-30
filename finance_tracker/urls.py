from django.urls import path
from django.contrib import admin
from . import views

app_name = 'finance_tracker'

urlpatterns = [
    # ex: /polls/
    path("", views.index_view, name="index"),
    path("dashboard/", views.dashboard_view, name= "dashboard"),
    path("accounts/", views.accounts_view, name= "accounts"),
    path("cashflow/", views.cashflow_view, name= "cashflow"),
    path("categories/", views.categories_view, name= "categories"),
    path("investments/", views.investments_view, name= "investments"),
    path("recurring/", views.recurring_view, name= "recurring"),
    path("transactions/", views.transactions_view, name= "transactions"),
]