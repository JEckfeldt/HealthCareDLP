from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from DoctorPortal.models import *
from django.core.exceptions import ValidationError  
from datetime import date
from . import logging

class NewPatientForm(UserCreationForm):

    class Meta:
        model = Patient
        exclude = ('createdAt', 'lastUpdated','allergies', 'history', 'symptoms', 'last_login', 'password', 'otp_verification_secret',)

    username = forms.CharField(label='username', min_length=5, max_length=100) 
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    ssn = forms.CharField(label='ssn', min_length=9, max_length=9) #ssn should be unique
    address = forms.CharField(label='address',max_length=200)

    # patient info all healthcare can see
    #id = models.BigAutoField(primary_key=True)
    #password = forms.CharField(max_length=50)
    #createdAt = models.DateTimeField(auto_now_add=True) # time the patient was created
    #lastUpdated = models.DateTimeField(auto_now=True) # time the patient info was last edited
    fname = forms.CharField(label='fname',max_length=50)
    lname = forms.CharField(label='lname',max_length=50)
    sex = forms.CharField(label='sex',max_length=1) # M or F
    #symptons = form.TextField() #large body of text
    age = forms.IntegerField(label='age') # 0 - 130 yrs old
    weight = forms.IntegerField(label='weight') # 1-2000lbs
    #allergies = models.TextField() # known allergies
    #history = models.TextField() # the medical history

   

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = Patient.objects.filter(username = username)  
        #if new.count():  
            #raise ValidationError("User Already Exist")  
        return username  
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        return password2
    
    def save(self, commit = True):  
        user = Patient()
        user.phone = 000000000
        user.ssn = self.cleaned_data['ssn']
        user.address = self.cleaned_data['address']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password2']
        user.createdAt = date.today()
        user.lastUpdated = date.today()
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.sex = self.cleaned_data['sex']
        user.symptons = ""
        user.age = self.cleaned_data['age']
        user.weight = self.cleaned_data['weight']
        user.allergies = ""
        user.history = ""
        user.is_doctor = False
        user.is_patient = True
        user.set_password(self.cleaned_data['password2'])
        user.otp_verification_secret='base32secret3232'
        user.is_active = True
        user.save()
        return user 
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    verification_code = forms.CharField(max_length=6)

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentFormPatient(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AppointmentFormPatient, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Appointments
        exclude = ('docNotes', 'apptDate', 'staffUser', 'patient', 'updaterUsername')
    
    apptDate = forms.DateField(label = 'Date of Appointment', widget=DateInput)
    mydoctor = forms.ModelChoiceField(
        queryset=Patient.objects.filter(is_doctor=True)
    )

    def save(self, commit = True):
        newAppt = Appointments()
        newAppt.staffUser = self.cleaned_data['mydoctor']
        newAppt.patient = self.user
        newAppt.apptDate = self.cleaned_data['apptDate']
        newAppt.patientNotes = self.cleaned_data['patientNotes']
        newAppt.save()
        return newAppt
    
class EditProfileFormPatient(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EditProfileFormPatient, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Patient
        exclude = ('createdAt', 'lastUpdated', 'last_login', 'password', 'username', 'fname', 'lname', 'is_patient', 'is_doctor', 'ssn', )

