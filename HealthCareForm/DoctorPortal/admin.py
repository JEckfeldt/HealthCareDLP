from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from PatientPortal.forms import NewPatientForm
from .models import Patient

# Register your models here.

class PatientAdmin(UserAdmin):
    add_form = NewPatientForm
    #form = CustomUserChangeForm
    model = Patient
    list_display = ["username",]
    list_filter = ['username',]
    filter_horizontal = ()

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )

admin.site.register(Patient, PatientAdmin)

