from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [ 
    path('admin/click', views.AdminClickTemplateView.as_view(), name='admin_click'),
    path('admin/signup', views.admin_signup_view, name='admin_signup'),
    path('admin/login', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/dashboard', views.admin_dashboard_view,name='admin_dashboard'),
    path('department/add/', views.DeparmentCreateview.as_view(),name='add_department'),
    path('dashboard/doctor/', views.AdminDoctorView.as_view(),name='dashboard_doctor'),
    path('dashboard/patient/', views.AdminPatientView.as_view(),name='dashboard_patient'),
    path('dashboard/appointment/', views.AdminAppointmentView.as_view(),name='dashboard_appointment'),
]
