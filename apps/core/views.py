from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    return render(request,'core/admin_dashboard.html', {})

@login_required
def store_admin(request):

    if request.user.user_type != 'STORE_ADMIN':
        return redirect('login')
    return render(request, "core/store_admin.html", {})

def index(request):
    return render(request, 'core/index.html', {})