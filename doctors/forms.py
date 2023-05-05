from django import forms
from django.contrib.auth import get_user_model
from .models import DoctorProfile

#for doctor related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model= DoctorProfile
        fields=['address','mobile','department','status','profile_pic']