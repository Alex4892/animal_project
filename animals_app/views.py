from django.shortcuts import render

def view_animals(request):
    return render(request, "animals/index.html")

# Create your views here.
