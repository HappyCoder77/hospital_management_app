from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name=''),
    path('admin-click',views.AdminClickTemplateView.as_view(),name='admin_click'),
    path('doctor-click',views.DoctorClickTemplateView.as_view(),name='doctor_click'),
    path('patient-click',views.PatientClickTemplateView.as_view(),name='patient_click'),
    path('about-us',views.AboutUsTemplateView.as_view(),name='about_us'),
    path('contact-us',views.contactus_view,name='contact_us'),
]