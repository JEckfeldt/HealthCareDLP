# Generated by Django 4.2.5 on 2023-11-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorPortal', '0018_alter_appointments_apptdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='apptDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]