from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# all models have a built in field "primary key" which is their unique id

# Patient model
class Patient(models.Model):
    #private patient info
    phone = models.IntegerField() # 1 (999)-999-9999 11 long
    ssn = models.PositiveIntegerField(unique=True) #ssn should be unique
    address = models.CharField(max_length=200, default= '')

    # patient info all healthcare can see
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True) # time the patient was created
    lastUpdated = models.DateTimeField(auto_now=True) # time the patient info was last edited
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    sex = models.CharField(max_length=1) # M or F
    symptons = models.TextField() #large body of text
    age = models.PositiveIntegerField(validators=[MaxValueValidator(130), MinValueValidator(0)]) # 0 - 130 yrs old
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2000)]) # 1-2000lbs
    allergies = models.TextField() # known allergies
    history = models.TextField() # the medical history

# Doctor model
class Doctor(models.Model):
    # a patient can see their doctor and this app doesnt deal with doctor info.
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    patients = models.ManyToManyField(Patient)

# Access Model (list of doctor patients etc)
# Used for access management and another layer of security
class PatientDoctor(models.Model):
    staffID = models.IntegerField(default=-1)
    patientID = models.IntegerField(default=-1)
    updaterID = models.IntegerField(default=-1)

    AccessLevelChoices = [('A', "Admin"), ('V', "Viewer")] #see all info or just necessary info
    AccessLevel = models.CharField(max_length=1, choices=AccessLevelChoices, default='V')

    lastUpdated = models.DateTimeField(auto_now=True) # time the patient info was last edited
    createdAt = models.DateTimeField(auto_now_add=True) # time the patient was created
    
