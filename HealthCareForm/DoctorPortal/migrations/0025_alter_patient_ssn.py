# Generated by Django 4.2.5 on 2023-11-24 21:50

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorPortal', '0024_alter_doctor_password_alter_patient_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=encrypted_model_fields.fields.EncryptedCharField(unique=True),
        ),
    ]
