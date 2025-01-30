from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request,"finance_tracker/index.html")

def dashboard_view(request):
    return render(request,"finance_tracker/dashboard.html")

def accounts_view(request):
    return render(request,"finance_tracker/accounts.html")

def cashflow_view(request):
    return render(request,"finance_tracker/cashflow.html")

def categories_view(request):
    return render(request,"finance_tracker/categories.html")

def investments_view(request):
    return render(request,"finance_tracker/investments.html")

def transactions_view(request):
    return render(request,"finance_tracker/transactions.html")

def recurring_view(request):
    return render(request,"finance_tracker/recurring.html")