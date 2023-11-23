from django.shortcuts import render, redirect
from .doctor_form import DoctorForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import logging
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.views import TOTPVerificationView
from .forms import Enable2FAForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
logger=logging.getLogger('custom')
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#from PatientPortal.views import loginUser

#login 

def our_login(request):
    return render(request, 'login.html', {})

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
    
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    # get upcoming appointments
    today = date.today()
    myAppts = Appointments.objects.filter(staffUser=current_user, apptDate__gte=today)
    return render(request, "homePage_doctor.html", context = {'user': current_user, "appts": myAppts})

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
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    allPatients = Patient.objects.filter(is_patient=True)
    return render(request, "addPatients_doctor.html", context = {'patients': allPatients})

def addPatient2(request, patientUsername):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
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
        return redirect(viewPatients)
    else:
        logging.debug(duplicate)
        logging.debug("Error: this PatientDoctor configuration already exists!")


    if current_user.is_doctor == False:
        logging.debug("ERROR: current user is not a doctor. You should be kicked out.")
    return render(request, "addPatients_doctor.html", context = {'patients': allPatients})

def viewPatients(request):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    myPatients = PatientDoctor.objects.filter(staffUser = current_user)
    #for p in myPatients:
        #logging.debug(p.patient.username)
    return render(request, 'viewPatients_doctor.html', context = {"patients": myPatients})

def scheduleAppointmentDoctor(request):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = AppointmentFormDoctor(user=current_user, data=request.POST)
        if form.is_valid():
            newAppt = form
            newAppt.staffUser = current_user
            newAppt.save()
            logging.debug("Successfully created a new appointment.")
            logger.info(f"Doctor {current_user} added a appointment with patient {form.cleaned_data['mypatient']}  Date/Time: {current_datetime}")
            return redirect('doctorHome')
    else:  
        form = AppointmentFormDoctor(user=current_user)  
    context = {  
        'form':form  
    }  
    return render(request, 'scheduleAppointment_doctor.html', context)

def viewFutureApppointmentsDoctor(request):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    today = date.today()
    myAppts = Appointments.objects.filter(staffUser=current_user, apptDate__gt=today)
    #for a in myAppts:
        #logging.debug('appt id: ' + str(a.id))
    return render(request, "viewFutureAppointmentsDoctor.html", context = {'user': current_user, "appts": myAppts})

def viewPastApppointmentsDoctor(request):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    today = date.today()
    myAppts = Appointments.objects.filter(staffUser=current_user, apptDate__lt=today)
    #for a in myAppts:
        #logging.debug('appt id: ' + str(a.id))
    return render(request, "viewPastAppointmentsDoctor.html", context = {'user': current_user, "appts": myAppts})

def addDiagnosis(request):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = DiagnosisForm(user=current_user, data=request.POST)
        if form.is_valid():
            newDiagnosis = form
            newDiagnosis.staffUser = current_user
            newDiagnosis.save()
            logger.info(f"Doctor {current_user} added a diagnosis for patient {form.cleaned_data['mypatient']}  Date/Time: {current_datetime}")
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
    logger.info(f"{current_user} logged out Date/Time: {current_datetime}")
    return HttpResponseRedirect('/login')

def editProfileDoctor(request, patientUsername):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    chosenPatient1 = Patient.objects.filter(username=patientUsername)
    chosenPatient = chosenPatient1[0]
    logging.debug(chosenPatient)
    if request.method == 'POST':
        form = EditProfileFormDoctor(user=current_user, data=request.POST, instance=chosenPatient)
        if form.is_valid() is True:
            chosenPatient.symptoms = form.cleaned_data['symptoms']
            chosenPatient.weight = form.cleaned_data['weight']
            chosenPatient.allergies = form.cleaned_data['allergies']
            chosenPatient.history = form.cleaned_data['history']
            chosenPatient.save()
            logging.debug(form.cleaned_data['symptoms'])
            logging.debug(form.cleaned_data['weight'])
            logging.debug(form.cleaned_data['allergies'])
            logging.debug(form.cleaned_data['history'])
            logging.debug("Successfully edited patient")
            logger.info(f"Doctor {current_user} edited patient profile {chosenPatient}  Date/Time: {current_datetime}")
            return redirect('viewPatients')
            
        else:
            return redirect('doctorHome')
    else:  
        form = EditProfileFormDoctor(user=current_user, instance=chosenPatient)  
    context = {  
        'form':form, 'user': current_user, 'patient': chosenPatient
    }  
    return render(request, 'editProfile_doctor.html', context)

def viewProfileDoctor(request, patientUsername):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    chosenPatient1 = Patient.objects.filter(username=patientUsername)
    chosenPatient = chosenPatient1[0]
    diagnoses = Diagnosis.objects.filter(patient=chosenPatient)
    return render(request, 'viewProfile_doctor.html', context = {'patient': chosenPatient, 'user': current_user, 'diagnoses': diagnoses})

def viewProfileDoctorSecure(request, patientUsername):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    chosenPatient1 = Patient.objects.filter(username=patientUsername)
    chosenPatient = chosenPatient1[0]
    diagnoses = Diagnosis.objects.filter(patient=chosenPatient)
    return render(request, 'viewProfileSecure_doctor.html', context = {'patient': chosenPatient, 'user': current_user, 'diagnoses': diagnoses})


def editAppointmentDoctor(request, patientUsername, apptID):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    chosenAppt1 = Appointments.objects.filter(id = apptID)
    chosenAppt = chosenAppt1[0]
    if (request.method == 'POST'):
        form = AppointmentFormDoctor(user=current_user, data=request.POST, instance=chosenAppt)
        if form.is_valid() is True:
            chosenAppt.apptDate = form.cleaned_data['apptDate']
            chosenAppt.docNotes = form.cleaned_data['docNotes']
            chosenAppt.patient = form.cleaned_data['mypatient']
            chosenAppt.save()
            logger.info(f"Doctor {current_user} edited patient appointment for {form.cleaned_data['mypatient']}  Date/Time: {current_datetime}")
        return redirect(viewFutureApppointmentsDoctor)
    else:
        form = AppointmentFormDoctor(user=current_user, instance=chosenAppt)    
    #logging.debug("PatientNotes from chosenAppt: " + chosenAppt.patientNotes)
    return render(request, 'editAppointments_patient.html', context = {'appt': chosenAppt, 'user': current_user, 'form': form})

def confirmPassword(request, patientUsername):
    current_user = request.user
    chosenPatient1 = Patient.objects.filter(username=patientUsername)
    chosenPatient = chosenPatient1[0]
    diagnoses = Diagnosis.objects.filter(patient=chosenPatient)
    form = confirmPasswordForm(data=request.POST or None)
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    if (request.method == 'POST' and form.is_valid()):
        #form = confirmPasswordForm(data=request.POST)
        temp = form.cleaned_data['password']
        temp2 = current_user.password
        logging.debug(temp)
        logging.debug(temp2)
        if check_password(temp, current_user.password):
            form2 = EditProfileFormDoctor(user=current_user, instance=chosenPatient)  
            context = {  
                'form':form2, 'user': current_user, 'patient': chosenPatient
            }  
            url = reverse('editProfileDoctor', kwargs={'patientUsername': patientUsername})
            #return redirect(mystr)
            return HttpResponseRedirect(url)
            #return render(request, 'editProfile_doctor.html', context)
        else:
            return render(request, 'viewProfileSecure_doctor.html', context = {'patient': chosenPatient, 'user': current_user, 'diagnoses': diagnoses})
    else:
        print(form.errors.as_data())
        #return render(request, 'viewProfileSecure_doctor.html', context = {'patient': chosenPatient, 'user': current_user, 'diagnoses': diagnoses})
    return render(request, 'confirmPasswordDoctor.html', context = {'form': form, 'user': current_user})

def textReveal(request, patientUsername):
    current_user = request.user
    if (current_user.is_doctor == False):
        return HttpResponseRedirect('/login')
    chosenPatient1 = Patient.objects.filter(username=patientUsername)
    chosenPatient = chosenPatient1[0]
    diagnoses = Diagnosis.objects.filter(patient=chosenPatient)
    return render(request, 'viewProfile_doctor.html', context = {'patient': chosenPatient, 'user': current_user, 'diagnoses': diagnoses})


@login_required
def enable_2fa(request):
    if request.method == 'POST': #we need to enable 2fa for this user
        form = Enable2FAForm(request.user, request.POST)
        if form.is_valid():
            #enable 2FA for the user
            device = TOTPDevice.objects.create(user=request.user)
            device.save()
            logging.debug(f"enabled the 2fa form for user {request.user}")
            return redirect('verify_2fa')
    else: #otherwise we can simply return the form to the user
        form = Enable2FAForm(request.user)

    return render(request, 'enable_2fa.html', {'form': form})

@login_required
def verify_2fa(request):
    if request.method == 'POST':
        # Handle the 2FA verification form submission
        return TOTPVerificationView.as_view()(request)

    devices = TOTPDevice.objects.filter(user=request.user)
    return render(request, 'verify_2fa.html', {'devices': devices})