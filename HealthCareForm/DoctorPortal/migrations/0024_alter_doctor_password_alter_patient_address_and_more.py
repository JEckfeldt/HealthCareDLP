# Generated by Django 4.2.5 on 2023-11-16 22:35

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorPortal', '0023_alter_appointments_apptdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='password',
            field=encrypted_model_fields.fields.EncryptedCharField(default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=encrypted_model_fields.fields.EncryptedCharField(default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='createdAt',
            field=encrypted_model_fields.fields.EncryptedDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastUpdated',
            field=encrypted_model_fields.fields.EncryptedDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=encrypted_model_fields.fields.EncryptedCharField(default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=encrypted_model_fields.fields.EncryptedIntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=encrypted_model_fields.fields.EncryptedPositiveIntegerField(unique=True),
        ),
    ]
