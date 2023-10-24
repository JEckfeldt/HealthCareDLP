from django.shortcuts import render, redirect
from .doctor_form import DoctorForm
from .models import Doctor

#login 

def login(request):
    return render(request, 'login.html', {})

# home view
def home(request):
    return render(request, 'home.html', {})

def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Doctor.objects.create(**data)
            return redirect('/')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'doctor_form': form})
