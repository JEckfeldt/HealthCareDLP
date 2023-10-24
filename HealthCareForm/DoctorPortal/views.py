from django.shortcuts import render, redirect
from .doctor_form import DoctorForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import logging
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from .forms import *
from django.http import HttpResponseRedirect


#from PatientPortal.views import loginUser

# home view
def doctorHome(request):
    #newDoc = Patient()
    #newDoc.phone = 000000000
    #newDoc.ssn = 000000000
    #newDoc.address = 2905
    #newDoc.username = "testDoc3"
    #newDoc.password = "Loki98012"
    #ewDoc.createdAt = date.today()
    #newDoc.lastUpdated = date.today()
    #newDoc.fname = "Tony"
    #newDoc.lname = "Fauci"
    #newDoc.sex = "M"
    #newDoc.symptons = ""
    #newDoc.age = 45
    #newDoc.weight = 160
    #newDoc.allergies = ""
    #newDoc.history = ""
    #newDoc.is_doctor = True
    #newDoc.is_patient = False
    #newDoc.set_password("Loki98012")
    #newDoc.is_active = True
    #newDoc.save()
    current_user = request.user
    logging.debug(current_user.username)
    if request.user.is_authenticated:
        logging.debug("Doc User is authenticated!")
    else:
        logging.debug("ERROR: USER Not AUtHENTICATED")
    return render(request, 'homePage_doctor.html', context = {'user': current_user})

def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Doctor.objects.create(**data)
            return redirect('home')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'doctor_form': form})

def addPatient(request):
    allPatients = Patient.objects.filter(is_patient=True)
    return render(request, "addPatients_doctor.html", context = {'patients': allPatients})

def addPatient2(request, patientUsername):
    current_user = request.user
    allPatients = Patient.objects.filter(is_patient=True)
    chosenPatient = Patient.objects.filter(username=patientUsername)
    #logging.debug("You have chosen Patient {}".format(chosenPatient[0]))
    #logging.debug("Pair for consideration: {} -- {}".format(current_user, chosenPatient[0]))
    duplicate = PatientDoctor.objects.filter(staffUser = current_user, patient = chosenPatient[0])
    if not duplicate:
        newPatientDoc = PatientDoctor()
        newPatientDoc.staffUser = current_user
        newPatientDoc.patient = chosenPatient[0]
        newPatientDoc.updaterUsername = current_user.username
        newPatientDoc.lastUpdated = date.today()
        newPatientDoc.createdAt = date.today()
        newPatientDoc.save()
    else:
        logging.debug(duplicate)
        logging.debug("Error: this PatientDoctor configuration already exists!")


    if current_user.is_doctor == False:
        logging.debug("ERROR: current user is not a doctor. You should be kicked out.")
    return render(request, "addPatients_doctor.html", context = {'patients': allPatients})

def viewPatients(request):
    current_user = request.user
    myPatients = PatientDoctor.objects.filter(staffUser = current_user)
    #for p in myPatients:
        #logging.debug(p.patient.username)
    return render(request, 'viewPatients_doctor.html', context = {"patients": myPatients})

def scheduleAppointmentDoctor(request):
    current_user = request.user
    if request.method == 'POST':
        form = AppointmentFormDoctor(user=current_user, data=request.POST)
        if form.is_valid():
            newAppt = form
            newAppt.staffUser = current_user
            newAppt.save()
            logging.debug("Successfully created a new appointment.")
            return redirect('doctorHome')
    else:  
        form = AppointmentFormDoctor(user=current_user)  
    context = {  
        'form':form  
    }  
    return render(request, 'scheduleAppointment_doctor.html', context)

def viewAppointmentsDoctor(request):
    current_user = request.user
    myAppts = Appointments.objects.filter(staffUser=current_user)
    return render(request, 'viewAppointments_doctor.html', context = {"appts": myAppts})

def addDiagnosis(request):
    current_user = request.user
    if request.method == 'POST':
        form = DiagnosisForm(user=current_user, data=request.POST)
        if form.is_valid():
            newDiagnosis = form
            newDiagnosis.staffUser = current_user
            newDiagnosis.save()
            logging.debug("Successfully created a new diagnosis.")
            return redirect('doctorHome')
    else:  
        form = DiagnosisForm(user=current_user)  
    context = {  
        'form':form  
    }  
    return render(request, 'addDiagnosis.html', context)

def logoutDoctor(request):
    current_user = request.user
    logout(request)
    return HttpResponseRedirect('/login')



