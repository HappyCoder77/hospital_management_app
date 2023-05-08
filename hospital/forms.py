from django import forms
from django.contrib.auth import get_user_model

#  admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
