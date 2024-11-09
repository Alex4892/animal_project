from django.shortcuts import render

def view_substack(request):
    return render(request, 'substack/substack.html')

# Create your views here.
