from django.shortcuts import render

from .models import Animal

def view_animals(request):
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }
    return render(request, "animals/index.html", context=context)

def view_detail_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    context = {
        "animal": animal
    }
    return render(request, "animals/detail_animal.html", context=context)

# Create your views here.
