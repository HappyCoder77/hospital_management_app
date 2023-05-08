from django import forms
from django.contrib.auth import get_user_model


# for contact us page
class ContactUsForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


#  admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
