from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.patient_signup_view, name="patient_signup"),
    path("login/", LoginView.as_view(template_name="patients/patientlogin.html"), name="patient_login"),
]