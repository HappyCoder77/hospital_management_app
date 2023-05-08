from django.conf import settings
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import TemplateView

from .forms import AdminSignupForm, ContactUsForm


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class AdminClickTemplateView(TemplateView):
    template_name = "hospital/adminclick.html"


class DoctorClickTemplateView(TemplateView):
    template_name = "doctors/doctorclick.html"


class PatientClickTemplateView(TemplateView):
    template_name = "patients/patientclick.html"


class AboutUsTemplateView(TemplateView):
    template_name = "aboutus.html"


def contactus_view(request):
    sub = ContactUsForm()
    if request.method == 'POST':
        sub = ContactUsForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently=False)
            return render(request, 'contactussuccess.html')
    return render(request, 'contactus.html', {'form': sub})


def admin_signup_view(request):
    form = AdminSignupForm()
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect(reverse("admin_login"))

    return render(request, 'hospital/adminsignup.html', {'form': form})
