from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login(request): 
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)

            if user.user_type == "ADMIN":
                return redirect("admin_dashboard")
            
            return HttpResponse(
                f"Username: f{request.user.username}, User type: f{request.user.user_type}")
    else:
        form = AuthenticationForm()
         
    return render(request, 'users/login.html', {'form':form})

def admin_dashboard(request):
    return render(request, "users/admin_dashboard.html", context= {})
