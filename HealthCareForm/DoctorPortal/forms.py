from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from DoctorPortal.models import *
from django.core.exceptions import ValidationError  
from datetime import date
from . import logging


class NewDoctorForm(UserCreationForm):

    class Meta:
        model = Doctor
        exclude = ('patients', 'otp_verification_secret',)

    username = forms.CharField(label='username', min_length=5, max_length=100) 
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    fname = forms.CharField(label='fname',max_length=50)
    lname = forms.CharField(label='lname',max_length=50)
    specialty = forms.CharField(label='specialty',max_length=50) # M or F
    #symptons = form.TextField() #large body of text
    #allergies = models.TextField() # known allergies
    #history = models.TextField() # the medical history

   

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = Doctor.objects.filter(username = username)  
        #if new.count():  
            #raise ValidationError("User Already Exist")  
        return username  
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        return password2
    
    def save(self, commit = True):  
        user = Doctor()
        #ser.phone = 000000000
        #user.ssn = self.cleaned_data['ssn']
        #user.address = self.cleaned_data['address']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password2']
        #user.createdAt = date.today()
        #user.lastUpdated = date.today()
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        #user.sex = self.cleaned_data['sex']
        #user.symptons = ""
        #user.age = self.cleaned_data['age']
        #user.weight = self.cleaned_data['weight']
        #user.allergies = ""
        #user.history = ""
        user.specialty = "na"
        user.set_password(self.cleaned_data['password2'])
        user.is_active = True
        user.save()
        return user 
    

class DateInput(forms.DateInput):
    input_type = 'date'

#class AppointmentFormDoctor(forms.Form):
    #apptDate = forms.DateField(label='Date of Appointment', widget=DateInput)
    #docNotes = forms.TimeField(label='Physician Notes')
    #user = forms.ModelChoiceField(
       #queryset=Patient.objects.filter(is_active=True)
   # )


class AppointmentFormDoctor(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AppointmentFormDoctor, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Appointments
        exclude = ('patientNotes', 'apptDate', 'staffUser', 'patient', 'updaterUsername')
    
    apptDate = forms.DateField(label = 'Date of Appointment', widget=DateInput(attrs={'class': 'apptDate'}))
    mypatient = forms.ModelChoiceField(
        queryset=Patient.objects.filter(is_patient=True)
    )

    def save(self, commit = True):
        newAppt = Appointments()
        newAppt.patient = self.cleaned_data['mypatient']
        newAppt.staffUser = self.user
        newAppt.apptDate = self.cleaned_data['apptDate']
        newAppt.docNotes = self.cleaned_data['docNotes']
        newAppt.save()
        return newAppt
    

class DiagnosisForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DiagnosisForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Diagnosis
        exclude = ('createdAt', 'lastUpdated', 'staffUser', 'patient', 'updaterUsername')
    
    mypatient = forms.ModelChoiceField(
        queryset=Patient.objects.filter(is_patient=True)
    )

    def save(self, commit = True):
        newDiagnosis = Diagnosis()
        newDiagnosis.patient = self.cleaned_data['mypatient']
        newDiagnosis.staffUser = self.user
        newDiagnosis.updaterUsername = self.user.username
        newDiagnosis.createdAt = date.today()
        newDiagnosis.lastUpdated = date.today()
        newDiagnosis.docNotes = self.cleaned_data['docNotes']
        newDiagnosis.diagnosis = self.cleaned_data['diagnosis']
        newDiagnosis.save()
        return newDiagnosis
    
class EditProfileFormDoctor(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EditProfileFormDoctor, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Patient
        exclude = ('createdAt', 'lastUpdated', 'staffUser', 'patient', 'updaterUsername', 'age', 'ssn', 'name', 'username', 'password', 'last_login', 'phone', 'address', 'fname', 'lname', 'is_doctor', 'is_patient', 'sex', 'otp_verification_secret',)
    



class confirmPasswordForm(forms.Form):
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)







