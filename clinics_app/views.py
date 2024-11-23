from django.shortcuts import render

from .models import Clinic


def view_detail_clinic(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinics/detail_clinics.html', {'clinics': clinics})

# Create your views here.
