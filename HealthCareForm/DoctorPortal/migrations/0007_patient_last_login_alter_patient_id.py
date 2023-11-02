# Generated by Django 4.2.5 on 2023-10-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DoctorPortal", "0006_patient_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
