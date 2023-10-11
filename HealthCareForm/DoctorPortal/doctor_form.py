from django import forms 

class DoctorForm(forms.Form):
    field1 = forms.CharField(label='Field 1')
    field2 = forms.IntegerField(label='Field 2')