from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Department, DoctorProfile


class DepartmentTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.department = Department.objects.create(
            name='Cardiologist',
        )

    def test_model_data(self):
        self.assertEqual(self.department.pk, 1)
        self.assertEqual(self.department.name, 'Cardiologist')

class DoctorProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="gregorio",
            email="gregorio@ejemplo.com",
            password="test1234"
        )

        cls.department = Department.objects.create(
            name='Cardiologist',
        )   

        cls.doctor_profile = DoctorProfile.objects.create(
            user = cls.user,
            profile_pic = "",
            address="Dirección",
            mobile="04265789874",
            department=cls.department,
        )

    def test_model_data(self):
        self.assertEqual(self.doctor_profile.pk, 1)
        self.assertEqual(self.doctor_profile.user.pk, self.user.pk)
        self.assertEqual(self.doctor_profile.department.pk, self.department.pk)
        self.assertEqual(self.doctor_profile.profile_pic, "") # TODO: arreglar esto con una imagen real
        self.assertEqual(self.doctor_profile.address, "Dirección")
        self.assertEqual(self.doctor_profile.mobile, "04265789874")
        self.assertFalse(self.doctor_profile.status)
        self.assertEqual(self.doctor_profile.get_name,
            f"{self.doctor_profile.user.first_name} {self.doctor_profile.user.last_name}"
        )
        self.assertEqual(self.doctor_profile.id, 1)
        self.assertEqual(
            self.doctor_profile.__str__(),
            f"Dr. {self.user.first_name} {self.user.last_name} ({self.department.name})"
        )


