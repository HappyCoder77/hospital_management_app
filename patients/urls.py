from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('patient-click', views.PatientClickTemplateView.as_view(), name='patient_click'),
    path("signup/", views.patient_signup_view, name="patient_signup"),
    path("login/", views.PatientLoginView.as_view(), name="patient_login"),
    path("dashboard/", views.patient_dashboard_view, name="patient_dashboard"),
]
