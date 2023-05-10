from django.db import models
from accounts.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pic/doctor_profile_pic/", null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "Dr. " + str(self.user.first_name) + " " + str(self.user.last_name) + " (" + str(self.department.name) + ")"
    