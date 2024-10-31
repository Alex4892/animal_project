from django.shortcuts import render, get_object_or_404

from .models import Animal

def view_animals(request):
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }
    return render(request, "animals/index.html", context=context)

def view_detail_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    kinds = animal.kinds.all()
    context = {
        "animal": animal,
        "kinds": kinds
    }
    return render(request, "animals/detail_animal.html", context=context)

# Create your views here.
