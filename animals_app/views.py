from django.shortcuts import render, get_object_or_404, redirect

from .models import Animal
from .forms import AnimalForm

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

def add_animal_view(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animals:index')
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})

def edit_animal_view(request, book_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animals:index')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animals/add_animal.html', {'form': form})

def delete_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    print(animal)
    if request.method == 'POST':
        animal.delete()
        return redirect('animals:index')
    return render(request, 'animals/delete_animal.html', {'animal': animal})

# Create your views here.
