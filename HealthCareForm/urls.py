# project/urls.py

from django.urls import path, include
from HealthCareForm.urls import urlpatterns as health_care_form_urls
from DoctorPortal.urls import urlpatterns as doctor_portal_urls
from PatientPortal.urls import urlpatterns as patient_portal_urls
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', include(tf_urls)),
    path('health_care_form/', include(health_care_form_urls)),
    path('doctor_portal/', include(doctor_portal_urls)),
    path('patient_portal/', include(patient_portal_urls)),
    path('two_factor/', include(tf_urls)),
    # other project-level URL patterns
]
