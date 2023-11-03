from django.shortcuts import render, redirect
from DoctorPortal.models import *
from django.contrib.auth import authenticate, login, logout
from .forms import NewPatientForm, LoginForm, AppointmentFormPatient, EditProfileFormPatient
from . import logging
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from DoctorPortal.views import doctorHome
from django.http import HttpResponseRedirect
from datetime import date

class CreatePatient(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['username', 'password', 'phone', 'ssn', 'fname', 'lname', 'sex', 'age', 'weight' ]
    template_name = 'create_new_patient.html'
    success_url = reverse_lazy('user_list')

def user_list(request):
    users = Patient.objects.all()
    return render(request, 'user_list.html', {'users': users})

# home view
def loginUser(request):
    form = LoginForm(data=request.POST or None)
    message = ""
    if request.method == 'POST' and form.is_valid():
        logging.debug("Username = {}".format(form.cleaned_data['username']))
        logging.debug("Password = {}".format(form.cleaned_data['password']))
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
            )

        if user is not None:
            logging.debug("Successful Login! Welcome!")
            login(request, user)
            messege = f"Successful Login! Welcome!"
            if user.is_patient == True:
                return redirect('patientHome')
            if user.is_doctor == True:
                return redirect('doctorHome')
        else:
            message = "Login Failed"
    return render(request, 'loginUser.html', context={'form': form, 'message': message})


def register(request):  
    logging.debug("Entering register...")
    patients = Patient.objects.all()
    for p in patients:
        print(p.username)
        print(p.password)
    if request.method == 'POST':  
        logging.debug("Entering request == post...")
        form = NewPatientForm(request.POST)  
        if form.is_valid():  
            logging.debug("Entering form is valid...")
            user = form.save()
            user.is_active = True
            user.save()
            logging.debug("Sucessfully added the user!")
            #return redirect('/login')
        else:
            logging.debug("Entering form is INVALID!")
            #logging.debug(form.error_messages)
            logging.debug(form.errors.as_data())
            #logging.debug(form.username)
            #logging.debug(form.password2)

    else:  
        form = NewPatientForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)  

def patientHome(request):
    current_user = request.user
    logging.debug(current_user.username)
    if request.user.is_authenticated:
        logging.debug("User is authenticated!")
        current_user = request.user
        today = date.today()
        myAppts = Appointments.objects.filter(patient=current_user, apptDate__gte=today)
        return render(request, "homePage_patient.html", context = {'user': current_user, "appts": myAppts})
    else:
        logging.debug("ERROR: USER Not AUtHENTICATED")
    
    # return render(request, 'homePage_patient.html', context = {'user': current_user})

def viewProfile(request):
    current_user = request.user
    diagnoses = Diagnosis.objects.filter(patient=current_user)
    return render(request, 'viewProfile_patient.html', context = {"user": current_user, "diagnoses": diagnoses})

def logoutPatient(request):
    current_user = request.user
    logout(request)
    return redirect('login')

def scheduleAppointmentPatient(request):
    current_user = request.user
    if request.method == 'POST':
        form = AppointmentFormPatient(user=current_user, data=request.POST)
        if form.is_valid():
            newAppt = form
            newAppt.patient = current_user
            newAppt.save()
            logging.debug("Successfully created a new appointment.")
            return redirect('patientHome')
    else:  
        form = AppointmentFormPatient(user=current_user)  
    context = {  
        'form':form  
    }  
    return render(request, 'scheduleAppointment_doctor.html', context)

def viewFutureApppointmentsPatient(request):
    current_user = request.user
    today = date.today()
    myAppts = Appointments.objects.filter(patient=current_user, apptDate__gte=today)
    #for a in myAppts:
        #logging.debug('appt id: ' + str(a.id))
    return render(request, "viewFutureAppointmentsPatient.html", context = {'user': current_user, "appts": myAppts})

def viewPastApppointmentsPatient(request):
    current_user = request.user
    today = date.today()
    myAppts = Appointments.objects.filter(patient=current_user, apptDate__lt=today)
    #for a in myAppts:
        #logging.debug('appt id: ' + str(a.id))
    return render(request, "viewPastAppointmentsPatient.html", context = {'user': current_user, "appts": myAppts})

def editAppointmentPatient(request, patientUsername, apptID):
    chosenAppt1 = Appointments.objects.filter(id = apptID)
    chosenAppt = chosenAppt1[0]
    current_user = request.user
    if (request.method == 'POST'):
        form = AppointmentFormPatient(user=current_user, data=request.POST, instance=chosenAppt)
        if form.is_valid() is True:
            chosenAppt.apptDate = form.cleaned_data['apptDate']
            chosenAppt.patientNotes = form.cleaned_data['patientNotes']
            chosenAppt.staffUser = form.cleaned_data['mydoctor']
            chosenAppt.save()
        return redirect(viewFutureApppointmentsPatient)
    else:
        form = AppointmentFormPatient(user=current_user, instance=chosenAppt)    
    #logging.debug("PatientNotes from chosenAppt: " + chosenAppt.patientNotes)
    return render(request, 'editAppointments_patient.html', context = {'appt': chosenAppt, 'user': current_user, 'form': form})

def editProfilePatient(request):
    current_user = request.user
    chosenProfile1 = Patient.objects.filter(username=current_user.username)
    chosenProfile = chosenProfile1[0]
    if (request.method == 'POST'):
        form = EditProfileFormPatient(user=current_user, data=request.POST, instance=chosenProfile)
        if form.is_valid() is True:
            chosenProfile.history = form.cleaned_data['history']
            chosenProfile.symptoms = form.cleaned_data['symptoms']
            chosenProfile.allergies = form.cleaned_data['allergies']
            chosenProfile.age = form.cleaned_data['age']
            chosenProfile.weight = form.cleaned_data['weight']
            chosenProfile.save()
            return redirect(viewProfile)
    else:
        form = EditProfileFormPatient(user=current_user, instance=chosenProfile)
    return render(request, 'editProfile_patient.html', context = {'user': current_user, 'profile': chosenProfile, 'form': form})



#exit notes:
# So, we have setup a custom user class that has been successfully authenticated! Great work. 
# what's next?
#  1) Do the same for Doctor. Add manager, create users inside a function(skip login page), confirm authentication
#  2) Allow Doctors to ADD patients to their list/relationship -- solidify relationship
#  3) Create Appointment and Diagnosis Models (End of Tuesday)
#  4) Allow Patients and Doctors to schedule Appointments, add Diagnosis (End of Wednesday)
#  5) Add Edit Profile functionality, work on CSS

#Final Notes:
# Things should be much smoother going forward. Doctor is more simplistic than Patient, with the exception
# of having a relation, but that's well documented. Appointment and Diagnosis are basic relation models comprised
# of simply text and dates and some FKs. Easy to handle. Final product: I want to log in as a user and see a list of my
# appointments and diagnoses, with the corresponding doctor and notes attached 
#Potential Issues:
# We could run into an issue with adding relations to Patient... but that should just be a horizontal filter addition.
# We could run into issues with the PatientDoctor table, but I am not convinced it's needed for MVP.
# 






    
