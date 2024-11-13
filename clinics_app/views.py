# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.core.exceptions import PermissionDenied
# from django.core.paginator import Paginator
# from django.views.decorators.http import require_POST
# from django.http import JsonResponse


# from .models import Clinic
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


# def view_detail_clinic(request):
#     clinic_animals = Clinic.objects.all()
#     context = {
#         'clinic_animals': clinic_animals
#     }
#     return render(request, 'clinics/detail_clinics.html', context)

# Create your views here.
