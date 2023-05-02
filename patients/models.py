from django.db import models

from accounts.models import CustomUser

class Patient(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
