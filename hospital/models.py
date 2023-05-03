from django.db import models

from patients.models import PatientProfile
from doctors.models import DoctorProfile


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile(), on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile(), on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)


class PatientDischargeDetails(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    # admitDate=models.DateField(null=False) # Esto hay que mejorarlo
    # releaseDate=models.DateField(null=False) # Esto hay que mejorarlo
    daySpent=models.PositiveIntegerField(null=False)
    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)
