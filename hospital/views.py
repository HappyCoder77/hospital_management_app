from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class AdminClickTemplateView(TemplateView):
    template_name = "hospital/adminclick.html"


class DoctorClickTemplateView(TemplateView):
    template_name = "hospital/doctorclick.html"


class PatientClickTemplateView(TemplateView):
    template_name = "hospital/patientclick.html"


class AboutUsTemplateView(TemplateView):
    template_name = "hospital/aboutus.html"