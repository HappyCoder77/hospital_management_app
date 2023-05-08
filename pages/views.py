from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactUsForm


class HomeTemplateView(TemplateView):
    template_name = "pages/index.html"


class AboutUsTemplateView(TemplateView):
    template_name = "pages/aboutus.html"


def contactus_view(request):
    sub = ContactUsForm()
    if request.method == 'POST':
        sub = ContactUsForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently=False)
            return render(request, 'contactussuccess.html')
    return render(request, 'pages/contactus.html', {'form': sub})
