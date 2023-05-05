from django.shortcuts import render
from .forms import PatientUserForm, PatientProfileForm
from django.contrib.auth.models import Group

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

        return HttpResponseRedirect('patientlogin')
    return render(request,'patients/patientsignup.html',context=mydict)