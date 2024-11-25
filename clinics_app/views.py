from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Clinic


def view_detail_clinic(request):
    groups_list = Clinic.objects.all()
    paginator = Paginator(groups_list, 10)
    page_number = request.GET.get('page')
    clinics = paginator.get_page(page_number)
    context = {
        "clinics": clinics
    }
    return render(request, 'clinics/detail_clinics.html', context=context)
    return render(request, 'clinics/detail_clinics.html', {'clinics': clinics})
# Create your views here.
