# Generated by Django 4.2 on 2023-05-03 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctors", "0002_rename_deparment_doctorprofile_department"),
        ("patients", "0002_rename_patient_patientprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientDischargeDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("admitDate", models.DateField()),
                ("releaseDate", models.DateField()),
                ("daySpent", models.PositiveIntegerField()),
                ("roomCharge", models.PositiveIntegerField()),
                ("medicineCost", models.PositiveIntegerField()),
                ("doctorFee", models.PositiveIntegerField()),
                ("OtherCharge", models.PositiveIntegerField()),
                ("total", models.PositiveIntegerField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patientprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now=True)),
                ("description", models.TextField(max_length=500)),
                ("status", models.BooleanField(default=False)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctors.doctorprofile",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patientprofile",
                    ),
                ),
            ],
        ),
    ]
