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
#app_name='patient'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('patientHome/', views.patientHome, name='patientHome'),
    path('viewProfile', views.viewProfile, name='viewProfile'),
    path('logoutPatient', views.logoutPatient, name='logoutPatient'),
    path('scheduleAppointmentPatient', views.scheduleAppointmentPatient, name='scheduleAppointmentPatient'),
    path('viewFutureAppointmentsPatient', views.viewFutureApppointmentsPatient, name='viewFutureAppointmentsPatient'),
    path('editAppointmentPatient/<str:patientUsername>/<int:apptID>', views.editAppointmentPatient, name='editAppointmentPatient'),
    path('editProfilePatient', views.editProfilePatient, name='editProfilePatient'),
    path('viewPastAppointmentsPatient', views.viewPastApppointmentsPatient, name='viewPastAppointmentsPatient'),
]
