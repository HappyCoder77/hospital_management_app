from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactUsForm

class HomeTemplateView(TemplateView):
    template_name = "index.html"


class AdminClickTemplateView(TemplateView):
    template_name = "hospital/adminclick.html"


class DoctorClickTemplateView(TemplateView):
    template_name = "hospital/doctorclick.html"


class PatientClickTemplateView(TemplateView):
    template_name = "hospital/patientclick.html"


class AboutUsTemplateView(TemplateView):
    template_name = "hospital/aboutus.html"


def contactus_view(request):
    sub = ContactUsForm()
    if request.method == 'POST':
        sub = ContactUsForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'contactus.html', {'form':sub})