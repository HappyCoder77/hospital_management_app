from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import DoctorUserForm, DoctorProfileForm


class DoctorClickTemplateView(TemplateView):
    template_name = "doctors/doctorclick.html"


def doctor_signup_view(request):
    userForm = DoctorUserForm()
    doctorForm = DoctorProfileForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}

    if request.method=='POST':
        userForm = DoctorUserForm(request.POST)
        doctorForm = DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'doctors/doctorsignup.html',context=mydict)
