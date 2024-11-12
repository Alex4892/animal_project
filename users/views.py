from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction

from animals_app.models import Animal
from comments_app.models import Comment
from .forms import CustomUserCreationForm, CustomAuthenticationForm


@login_required(login_url='users:login')
def view_profile(request):
    user_animals = Animal.objects.filter(submit=request.user)
    return render(request, 'users/profile.html',
                           {'user_animals': user_animals})


def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required(login_url='users:login')
@user_passes_test(is_admin)
def view_admin_dashboard(request):
    animals = Animal.objects.filter(is_verified=False)
    comments = Comment.objects.filter(is_verified=False)
    context = {
        'animals': animals,
        'comments': comments
    }
    return render(request, 'users/admin.html', context)


@transaction.atomic
def register_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animals:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('animals:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('animals:index')

# Create your views here.
