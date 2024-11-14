from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest, HttpResponse


from .models import Animal
from .forms import AnimalForm
from comments_app.forms import CommentForm


def view_animals(request: HttpRequest) -> HttpResponse:
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
def add_animal_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.submit = request.user
            animal.save()
            targets = form.cleaned_data.get('target')
            animal.target.set(targets)
            animal.save()
            kinds = form.cleaned_data.get('kind')
            animal.kind.set(kinds)
            animal.save()
            return redirect('animals:index')
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})


@login_required(login_url='users:login')
def edit_animal_view(request: HttpRequest, animal_id: int) -> HttpResponse:
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.submit != request.user:
        raise PermissionDenied(
            "У вас нет прав на редактирование данного объявления.")
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animals:detail_animal', animal_id=animal.id)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animals/add_animal.html', {'form': form})

def filtered_animals_view(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()
    target = request.GET.get('target', '').strip()
    kind = request.GET.get('kind', '').strip()
    print(kind)
    if target:
        animals = animals.filter(target__name__icontains=target)
    if kind:
        animals = animals.filter(kind__name__icontains=kind)
    paginator = Paginator(animals, 8) 
    page_number = request.GET.get('page')
    animals_page = paginator.get_page(page_number)
    context = {
        'animals': animals_page
    }
    return render(request, 'animals/filtered_animals.html', context)


@login_required(login_url='users:login')
def delete_animal_view(request: HttpRequest, animal_id: int) -> HttpResponse:
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.submit != request.user:
        raise PermissionDenied(
            "У вас нет прав на редактирование данного объявления.")
    if request.method == 'POST':
        animal.delete()
        return redirect('animals:index')
    return render(request, 'animals/delete_animal.html', {'animal': animal})


@user_passes_test(lambda u: u.is_superuser)
@require_POST
def change_animal_status(request: HttpRequest, animal_id: int) -> JsonResponse:
    try:
        animal = Animal.objects.get(id=animal_id)
        animal.is_verified = not animal.is_verified
        animal.save()
        return JsonResponse({"status": "success",
                            "is_verified": animal.is_verified})
    except Animal.DoesNotExist:
        return JsonResponse({"status": "error",
                             "message": "Объявление не найдено"})
# Create your views here.
