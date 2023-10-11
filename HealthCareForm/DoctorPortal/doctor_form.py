from django import forms 

class DoctorForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=50)
    lname = forms.CharField(label='Last Name', max_length=50)