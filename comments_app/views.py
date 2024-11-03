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

# Create your views here.
