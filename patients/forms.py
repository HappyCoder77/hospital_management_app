from django import forms
from django.contrib.auth import get_user_model
from .models import PatientProfile

class PatientUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['address','mobile','status','profile_pic']