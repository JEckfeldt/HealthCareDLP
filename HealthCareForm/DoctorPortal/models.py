from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from .managers import PatientManager, DoctorManager
from encrypted_model_fields.fields import EncryptedCharField,EncryptedTextField,EncryptedIntegerField,EncryptedDateTimeField,EncryptedPositiveIntegerField

# all models have a built in field "primary key" which is their unique id


# Patient model
class Patient(AbstractBaseUser):
    #private patient info
    phone = EncryptedIntegerField() # 1 (999)-999-9999 11 long
    ssn = EncryptedCharField(unique=True, max_length=9) #ssn should be unique
    address = EncryptedCharField(max_length=200, default= '')

    # patient info all healthcare can see
    #id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, default = '', unique=True)
    password = EncryptedCharField(max_length=25, default='')
    createdAt = EncryptedDateTimeField(auto_now_add=True) # time the patient was created
    lastUpdated = EncryptedDateTimeField(auto_now=True) # time the patient info was last edited
    fname = models.CharField(max_length=50)
    lname = EncryptedCharField(max_length=50)
    sex = models.CharField(max_length=1) # M or F
    symptoms = EncryptedTextField(default='na') #large body of text
    age = models.PositiveIntegerField(validators=[MaxValueValidator(130), MinValueValidator(0)], default=None) # 0 - 130 yrs old
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2000)], default=None) # 1-2000lbs
    allergies = EncryptedTextField(default='na') # known allergies
    history = EncryptedTextField(default='na') # the medical history
    otp_verification_secret = EncryptedCharField(max_length=50, default='')

    is_patient = models.BooleanField('patientStatus', default=True)
    is_doctor = models.BooleanField('doctorStatus', default=False)

    objects = PatientManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.is_patient == True:
            return self.lname + ", " + self.fname
        elif (self.is_doctor == True):
            return "Dr." + self.fname + " " + self.lname
        else:
            return self.username


# We Don't Use Doctor
# Doctor model
class Doctor(AbstractBaseUser):
    # a patient can see their doctor and this app doesnt deal with doctor info.
    #id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, default = '', unique=True)
    password = EncryptedCharField(max_length=25, default='')
    fname = models.CharField(max_length=50, default='')
    lname = EncryptedCharField(max_length=50, default='')
    specialty = models.CharField(max_length=50, default='')
    patients = models.ManyToManyField(Patient)

    objects = DoctorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "Dr." + self.fname + " " + self.lname

# Access Model (list of doctor patients etc)
# Used for access management and another layer of security
class PatientDoctor(models.Model):
    staffUser = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctorUser', default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientUser', default='')
    updaterUsername = models.CharField(max_length=100, default = '')

    AccessLevelChoices = [('A', "Admin"), ('V', "Viewer")] #see all info or just necessary info
    AccessLevel = models.CharField(max_length=1, choices=AccessLevelChoices, default='V')

    lastUpdated = EncryptedDateTimeField(auto_now=True) # time the patient info was last edited
    createdAt = EncryptedDateTimeField(auto_now_add=True) # time the patient was created

    def __str__(self):
        return "Dr." + self.staffUser.lname + " -- Patient: " + self.patient.username

class Appointments(models.Model):
    staffUser = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='attendingDoctor', default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='apptPatient', default='')
    updaterUsername = models.CharField(max_length=100, default = '')
    apptDate = models.DateTimeField(auto_now_add=True)
    docNotes = EncryptedTextField(default='na') #large body of text
    patientNotes = EncryptedTextField(default='na') #large body of text

    def __str__(self):
        return "Appointment: Date: " + str(self.apptDate) + ", Doctor: " + self.staffUser.fname + " " + self.staffUser.lname + ", Patient: " + self.patient.username

class Diagnosis(models.Model):
    staffUser = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnosingDoctor', default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnosedPatient', default='')
    updaterUsername = models.CharField(max_length=100, default = '')
    diagnosis = EncryptedCharField(max_length=200, default='')
    docNotes = EncryptedTextField(default='na') #large body of text
    lastUpdated = EncryptedDateTimeField(auto_now=True) # time the diagnosis info was last edited
    createdAt = EncryptedDateTimeField(auto_now_add=True) # time the diagnosis was created

    def __str__(self):
        return "Appointment: Date: " + str(self.apptDate) + ", Doctor: " + self.staffUser.fname + " " + self.staffUser.lname + ", Patient: " + self.patient.username

    
