from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from .forms import CommentForm
from animals_app.models import Animal

def add_comment_view(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.animal = animal
            comment.save()
            return redirect('animals:detail_animal', animal_id=animal.id)
    else:
        form = CommentForm()
    return redirect('animals:detail_animal', animal_id=animal.id)

def edit_comment_view(request, comment_id, animal_id):
    comment = get_object_or_404(Comment, id=comment_id, animal_id=animal_id)
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('animals:detail_animal', animal_id=animal_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html', {'form': form, 'animal': animal, 'comment': comment})
def delete_comment_view(request, comment_id, animal_id):
    comment = get_object_or_404(Comment, id=comment_id, animal_id=animal_id)
    comment.delete()
    return redirect('animals:detail_animal', animal_id=animal_id)

# Create your views here.
