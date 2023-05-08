from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup', views.doctor_signup_view, name="doctor_signup"),
    path('login', LoginView.as_view(template_name="doctors/doctorlogin.html"), name="doctor_login"),
    path('doctor-click', views.DoctorClickTemplateView.as_view(), name='doctor_click'),
]
