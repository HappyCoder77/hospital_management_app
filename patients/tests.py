from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import PatientProfile


class PacientProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="camila",
            email="camila@ejemplo.com",
            password="test1234"
        )

        cls.patient_profile = PatientProfile.objects.create(
            user = cls.user,
            profile_pic = "",
            address="Dirección",
            mobile="04265789874",
        )

    def test_model_data(self):
        self.assertEqual(self.patient_profile.pk, 1)
        self.assertEqual(self.patient_profile.user.pk, self.user.pk)
        self.assertEqual(self.patient_profile.profile_pic, "") # TODO: arreglar esto con una imagen real
        self.assertEqual(self.patient_profile.address, "Dirección")
        self.assertEqual(self.patient_profile.mobile, "04265789874")
        self.assertFalse(self.patient_profile.status)
        self.assertEqual(self.patient_profile.get_name,
            f"{self.patient_profile.user.first_name} {self.patient_profile.user.last_name}"
        )
        self.assertEqual(self.patient_profile.get_id, self.patient_profile.user.id)
        self.assertEqual(
            self.patient_profile.__str__(),
            f"{self.patient_profile.user.first_name} {self.patient_profile.user.last_name}"
        )