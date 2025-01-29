from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance_tracker:index')
    else:    
        form = CustomUserCreationForm() 
    return render(request,"users/register.html", {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm( data=request.POST)
        if form.is_valid():
            return redirect("finance_tracker:index")  # Redirect to homepage
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})