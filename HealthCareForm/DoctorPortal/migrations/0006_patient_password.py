# Generated by Django 4.2.5 on 2023-10-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DoctorPortal", "0005_patient_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="password",
            field=models.CharField(default="", max_length=25),
        ),
    ]
