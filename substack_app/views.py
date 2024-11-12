from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Substack
from animals_app.models import Animal


@login_required(login_url='users:login')
def view_substack(request):
    substack_animals = Substack.objects.all()
    context = {
        'substack_animals': substack_animals
    }
    return render(request, 'substack/substack.html', context)


@require_POST
@login_required(login_url='users:login')
def add_to_substack(request):
    animal_id = request.POST.get("animal_id")
    try:
        animal = Animal.objects.get(id=animal_id)
        if animal.quantity == 0:
            return JsonResponse({"status": "error",
                                 "message": "В остатке нет объявлений"})
        substack_item, created = Substack.objects.get_or_create(
            user=request.user, animal=animal)
        if not created:
            substack_item.quantity += 1
            substack_item.save()
        return JsonResponse({"status": "success", "message":
                            "Объявление добавлено в закладку"})
    except Animal.DoesNotExist:
        return JsonResponse({"status": "error",
                             "message": "Объявление не найдено"})


@require_POST
@login_required(login_url='users:login')
def remove_from_substack(request):
    if request.method == "POST":
        substack_animal_id = request.POST.get("substack_animal_id")
        try:
            substack_animal = Substack.objects.get(id=substack_animal_id)
            substack_animal.delete()
            return JsonResponse({"status": "success",
                                 "message": "Объявление удалено из закладки"})
        except Animal.DoesNotExist:
            return JsonResponse({"status": "error",
                                 "message": "Объявление не найдено"})
    return JsonResponse({"status": "error", "message": "Некорректный запрос"})

# Create your views here.
