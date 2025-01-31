from django.shortcuts import render
from .models import Account
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return render(request,"finance_tracker/index.html")

@login_required
def dashboard_view(request):
    accounts = Account.objects.all()

    return render(request,"finance_tracker/dashboard.html",{"accounts":accounts})
@login_required

def accounts_view(request):
    accounts = Account.objects.all()
    return render(request,"finance_tracker/accounts.html",{"accounts":accounts})

@login_required
def cashflow_view(request):
    login_required
    return render(request,"finance_tracker/cashflow.html")

@login_required
def categories_view(request):
    return render(request,"finance_tracker/categories.html")

@login_required
def investments_view(request):
    return render(request,"finance_tracker/investments.html")

@login_required
def transactions_view(request):
    return render(request,"finance_tracker/transactions.html")

@login_required
def recurring_view(request):
    return render(request,"finance_tracker/recurring.html")