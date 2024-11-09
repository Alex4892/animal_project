from django.urls import path

from .views import view_substack

app_name = "substack"

urlpatterns = [
    path('substack/', view_substack, name='substack'),
]