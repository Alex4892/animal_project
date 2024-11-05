from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator


from .models import Animal
from .forms import AnimalForm
from comments_app.forms import CommentForm

def view_animals(request):
    animals_list = Animal.objects.all()
    paginator = Paginator(animals_list, 8)
    page_number = request.GET.get('page')
    animals = paginator.get_page(page_number)
    context = {
        "animals": animals
    }
    return render(request, "animals/index.html", context=context)

def view_detail_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    kinds = animal.kind.all()
    comments = animal.comments.all()
    form = CommentForm()
    context = {
        "animal": animal,
        "kinds": kinds,
        "comments": comments,
        "form": form,
    }
    return render(request, "animals/detail_animals.html", context=context)

@login_required(login_url='users:login')
def add_animal_view(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.submit = request.user
            animal.save() 
            return redirect('animals:index')
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})

@login_required(login_url='users:login')
def edit_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.submit != request.user:
        raise PermissionDenied(
            "У вас нет прав на редактирование данного объявления."
    )
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animals:detail_animal', animal_id=animal.id)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animals/add_animal.html', {'form': form})

@login_required(login_url='users:login')
def delete_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.submit != request.user:
        raise PermissionDenied(
            "У вас нет прав на редактирование данного объявления."
    )
    if request.method == 'POST':
        animal.delete()
        return redirect('animals:index')
    return render(request, 'animals/delete_animal.html', {'animal': animal})

# Create your views here.
