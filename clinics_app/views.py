from django.shortcuts import render

from .models import Clinic
# from .forms import ClinicForm


# def view_clinics(request):
#     # animals_list = Animal.objects.all()
#     # paginator = Paginator(animals_list, 8)
#     # page_number = request.GET.get('page')
#     # animals = paginator.get_page(page_number)
#     context = {
#         "animals": animals
#     }
#     return render(request, "animals/index.html", context=context)


def view_detail_clinic(request):
    clinic = Clinic.objects.all()
    name_clinic = clinic.name_clinic.all()
    adress = clinic.adress.all()
    context = {
        'clinic': clinic,
        'name_clinic': name_clinic,
        'adress': adress,
    }
    return render(request, 'clinics/detail_clinics.html', context)

# Create your views here.
