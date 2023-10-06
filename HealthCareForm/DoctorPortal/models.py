from django.db import models

# Create your models here.
# Patient model

class Doctor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

class Patient(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)