from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # user_type bo‘yicha yo‘naltirish
            if user.user_type == 'ADMIN':
                return redirect('admin_dashboard')
            elif user.user_type == 'STORE_ADMIN':
                return redirect('store_admin')
            else:
                return redirect('index')  # Clientlar uchun

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
