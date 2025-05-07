from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import my_login

urlpatterns = [
    path('login/', my_login, name='login'),

#     path('login/', auth_views.LogoutView.as_view(next_page='login'),
#          name='logout'),

#     path ('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
#     path('store-admin-dashboard/', views.store_admin_dashboard,
#          name='store_admin_dashboard'),
         
#     path('store/', views.store, name='store')
]
