from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [
    
    path('admin-click', views.AdminClickTemplateView.as_view(), name='admin_click'),
    path('admin-signup', views.admin_signup_view, name='admin_signup'),
    path('admin-login', views.AdminLoginView.as_view(), name='admin_login'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
]
