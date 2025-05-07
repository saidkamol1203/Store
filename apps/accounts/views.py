from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# @login_required

# @login_required
# def store_admin_dashboard(request):
#     return render(request,'users/store_admin_dashboard.html')

# def store(request):
#     return render(request,'users/store.html')

