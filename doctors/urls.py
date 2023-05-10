from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup', views.doctor_signup_view, name="doctor_signup"),
    path('login', views.DoctorLoginView.as_view(), name="doctor_login"),
    path('dashboard', views.doctor_dashboard_view, name="doctor_dashboard"),
    path('doctor-click', views.DoctorClickTemplateView.as_view(), name='doctor_click'),
]
