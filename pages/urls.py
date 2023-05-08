from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name=''),
    path('about-us', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact-us', views.contactus_view, name='contact_us'),
]