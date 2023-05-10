from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import PatientUserForm, PatientProfileForm
from .models import PatientProfile

class PatientClickTemplateView(TemplateView):
    template_name = "patients/patientclick.html"


def patient_signup_view(request):
    userForm = PatientUserForm()
    patientForm = PatientProfileForm()
    mydict={'userForm':userForm,'patientForm':patientForm}

    if request.method == 'POST':
        userForm = PatientUserForm(request.POST)
        patientForm= PatientProfileForm(request.POST,request.FILES)

        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user=user
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect(reverse("patient_login"))
    return render(request,'patients/patientsignup.html',context=mydict)


class PatientLoginView(LoginView):
    template_name = "patients/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
         return reverse_lazy('patient_dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


@login_required(login_url='patient_login')
# @user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=PatientProfile.objects.get(user_id=request.user.id)
    mydict={
    'patient':patient,
    'admitDate':patient.admitDate,
    }
    return render(request,'patients/patient_dashboard.html',context=mydict)