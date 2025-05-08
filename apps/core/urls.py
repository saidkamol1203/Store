from django.urls import path
from .views import admin_dashboard, index, store_admin

urlpatterns = [
    path('', index, name='index'),
    path('store/admin/', store_admin, name='store_admin'),
    path('super/admin/', admin_dashboard, name='admin_dashboard'),
]


 