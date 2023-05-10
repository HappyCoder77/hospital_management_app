from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from doctors.models import DoctorProfile
from hospital.models import Appointment, PatientDischargeDetails
from patients.models import PatientProfile
from .forms import DoctorUserForm, DoctorProfileForm



class DoctorClickTemplateView(TemplateView):
    template_name = "doctors/doctorclick.html"


def doctor_signup_view(request):
    userForm = DoctorUserForm()
    doctorForm = DoctorProfileForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}

    if request.method=='POST':
        userForm = DoctorUserForm(request.POST)
        doctorForm = DoctorProfileForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect(reverse("doctor_login"))
    return render(request,'doctors/doctorsignup.html',context=mydict)


class DoctorLoginView(LoginView):
    template_name = "doctors/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
         return reverse_lazy('doctor_dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


@login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount= PatientProfile.objects.all().filter(status=True,).count()
    appointmentcount= Appointment.objects.all().filter(status=True,doctor__id=request.user.id).count()
    patientdischarged= PatientDischargeDetails.objects.all()

    #for  table in doctor dashboard
    appointments= Appointment.objects.all().filter(status=True,doctor__id=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=PatientProfile.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor': DoctorProfile.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'doctors/doctor_dashboard.html',context=mydict)