from django.urls import path
from .views import login, admin_dashboard

urlpatterns = [
    path('login/', login, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),

] 

