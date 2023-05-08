from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from pages.forms import ContactUsForm
from .forms import AdminSignupForm
from .models import DoctorProfile, PatientProfile, Appointment


class AdminClickTemplateView(TemplateView):
    template_name = "hospital/adminclick.html"


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


class AdminLoginView(LoginView):
    template_name = "hospital/adminlogin.html"
    redirect_authenticated_user = True

    def get_success_url(self):
         return reverse_lazy('admin-dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


@login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors = DoctorProfile.objects.all().order_by('-id')
    patients = PatientProfile.objects.all().order_by('-id')
    #for three cards
    doctorcount = DoctorProfile.objects.all().filter(status=True).count()
    pendingdoctorcount= DoctorProfile.objects.all().filter(status=False).count()

    patientcount = PatientProfile.objects.all().filter(status=True).count()
    pendingpatientcount = PatientProfile.objects.all().filter(status=False).count()

    appointmentcount = Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount = Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)
