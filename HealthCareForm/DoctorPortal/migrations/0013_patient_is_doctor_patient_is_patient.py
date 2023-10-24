# Generated by Django 4.2.5 on 2023-10-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "DoctorPortal",
            "0012_doctor_last_login_doctor_password_doctor_patients_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="is_doctor",
            field=models.BooleanField(default=False, verbose_name="doctoStatus"),
        ),
        migrations.AddField(
            model_name="patient",
            name="is_patient",
            field=models.BooleanField(default=True, verbose_name="patientStatus"),
        ),
    ]