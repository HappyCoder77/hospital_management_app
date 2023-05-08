from django.contrib.auth import get_user_model
from django.test import TestCase

from doctors.models import Department, DoctorProfile
from patients.models import PatientProfile

from .models import Appointment, PatientDischargeDetails


class PacientProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="camila",
            email="camila@ejemplo.com",
            password="test1234"
        )
        cls.user2 = get_user_model().objects.create_user(
            username="anibal",
            email="anibal@ejemplo.com",
            password="test1234"
        )

        cls.department = Department.objects.create(
            name='Cardiologist',
        )

        cls.patient_profile = PatientProfile.objects.create(
            user=cls.user,
            profile_pic="",
            address="Dirección",
            mobile="04265789874",
        )

        cls.doctor_profile = DoctorProfile.objects.create(
            user=cls.user2,
            profile_pic="",
            address="Dirección",
            mobile="04265789874",
            department=cls.department,
        )

        cls.appointment = Appointment.objects.create(
            patient=cls.patient_profile,
            doctor=cls.doctor_profile,
            description="Descripción"
        )

    def test_model_data(self):
        self.assertEqual(self.appointment.pk, 1)
        self.assertEqual(self.appointment.patient.pk, self.patient_profile.pk)
        self.assertEqual(self.appointment.doctor.pk, self.doctor_profile.pk)
        self.assertEqual(self.appointment.description, "Descripción")
        self.assertFalse(self.appointment.status)


class PatientDischargeDetailsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="camila",
            email="camila@ejemplo.com",
            password="test1234"
        )

        cls.patient_profile = PatientProfile.objects.create(
            user=cls.user,
            profile_pic="",
            address="Dirección",
            mobile="04265789874",
        )

        cls.patientdischargedetails = PatientDischargeDetails.objects.create(
            patient=cls.patient_profile,
            # admitDate = timezone.now()
            # releaseDate =
            daySpent=2,
            roomCharge=100,
            medicineCost=25,
            doctorFee=40,
            OtherCharge=10,
            total=145
        )

    def test_model_data(self):
        self.assertEqual(self.patientdischargedetails.pk, 1)
        self.assertEqual(self.patientdischargedetails.patient.pk, self.patient_profile.pk)
        self.assertEqual(self.patientdischargedetails.daySpent, 2)
        self.assertEqual(self.patientdischargedetails.roomCharge, 100)
        self.assertEqual(self.patientdischargedetails.medicineCost, 25)
        self.assertEqual(self.patientdischargedetails.doctorFee, 40)
        self.assertEqual(self.patientdischargedetails.OtherCharge, 10)
        self.assertEqual(self.patientdischargedetails.total, 145)
