from django.urls import path
from apps.core.views import admin_dashboard, store_admin  # 'core' appidan import qilish

from .views import my_login

urlpatterns = [
    path('login/', my_login, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('store_admin/', store_admin, name='store_admin'),
]