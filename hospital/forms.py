from django import forms
from django.contrib.auth import get_user_model


from doctors.models import Department


#  admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"