from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpResponse, HttpRequest

from .models import Comment
from .forms import CommentForm
from animals_app.models import Animal


def add_comment_view(request: HttpRequest, animal_id: int) -> HttpResponse:
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.animal_id = animal_id
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            return redirect('animals:detail_animal', animal_id=animal.id)
    else:
        form = CommentForm()
    return redirect('animals:detail_animal', animal_id=animal.id)


def edit_comment_view(request: HttpRequest,
                      comment_id: int, animal_id: int) -> HttpResponse:
    comment = get_object_or_404(Comment, id=comment_id, animal_id=animal_id)
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('animals:detail_animal', animal_id=animal_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html',
                  {'form': form, 'animal': animal, 'comment': comment})


def delete_comment_view(request: HttpRequest,
                        comment_id: int, animal_id: int) -> HttpResponse:
    comment = get_object_or_404(Comment, id=comment_id, animal_id=animal_id)
    comment.delete()
    return redirect('animals:detail_animal', animal_id=animal_id)


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def change_comment_status(request: HttpRequest,
                          comment_id: int) -> JsonResponse:
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.is_verified = not comment.is_verified
        comment.save()
        return JsonResponse({"status": "success",
                            "is_verified": comment.is_verified})
    except Comment.DoesNotExist:
        return JsonResponse({"status": "error",
                            "message": "Комментарий не найден"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

# Create your views here.
