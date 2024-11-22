from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Favorite
from animals_app.models import Animal


@login_required(login_url='users:login')
def view_favorite(request: HttpRequest) -> HttpResponse:
    favorite_animals = Favorite.objects.filter(user=request.user)
    context = {
        'favorite_animals': favorite_animals
    }
    return render(request, 'favorites/favorites.html', context)


@require_POST
@login_required(login_url='users:login')
def add_to_favorite(request: HttpRequest) -> JsonResponse:
    animal_id = request.POST.get("animal_id")
    try:
        animal = Animal.objects.get(id=animal_id)
        if animal == 0:
            return JsonResponse({"status": "error",
                                 "message": "В остатке нет объявлений"})
        favorite_item, created = Favorite.objects.get_or_create(
            user=request.user, animal=animal)
        if not created:
            favorite_item.save()
        return JsonResponse({"status": "success", "message":
                            "Объявление добавлено в избранные"})
    except Favorite.DoesNotExist:
        return JsonResponse({"status": "error",
                             "message": "Объявление не найдено"})


@require_POST
@login_required(login_url='users:login')
def remove_from_favorite(request: HttpRequest) -> JsonResponse:
    favorite_animal_id = request.POST.get("favorite_animal_id")
    try:
        favorite_animal = Favorite.objects.get(id=favorite_animal_id)
        favorite_animal.delete()
        return JsonResponse({"status": "success",
                             "message": "Объявление удалено из избранных"})
    except Favorite.DoesNotExist:
        return JsonResponse({"status": "error",
                             "message": "Объявление не найдено"})

# Create your views here.
