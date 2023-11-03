"""
URL configuration for HealthCareForm project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
#app_name='doctor'



urlpatterns = [
    
    path('home', views.doctorHome, name='doctorHome'),
    path('doctor_form/', views.doctor_form, name='doctor_form'),
    path('addPatient', views.addPatient, name='addPatient'),
    path('addPatient/<str:patientUsername>/', views.addPatient2, name='addPatient2'),
    path('viewPatients', views.viewPatients, name='viewPatients'),
    path('scheduleAppointmentDoctor', views.scheduleAppointmentDoctor, name='scheduleAppointmentDoctor'),
    path('viewFutureAppointmentsDoctor', views.viewFutureApppointmentsDoctor, name='viewFutureAppointmentsDoctor'),
    path('viewPastAppointmentsDoctor', views.viewPastApppointmentsDoctor, name='viewPastAppointmentsDoctor'),
    path('addDiagnosis', views.addDiagnosis, name='addDiagnosis'),
    path('logoutDoctor', views.logoutDoctor, name='logoutDoctor'),
    path('editProfileDoctor/<str:patientUsername>/', views.editProfileDoctor, name='editProfileDoctor'),
    path('editAppointmentDoctor/<str:patientUsername>/<int:apptID>', views.editAppointmentDoctor, name='editAppointmentDoctor'),
    path('viewProfileDoctor/<str:patientUsername>', views.viewProfileDoctor, name='viewProfileDoctor'),
]
