# Generated by Django 4.2.5 on 2023-10-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DoctorPortal", "0008_rename_symptons_patient_symptoms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="username",
            field=models.CharField(default="", max_length=100, unique=True),
        ),
    ]
