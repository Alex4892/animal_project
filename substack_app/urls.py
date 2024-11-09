from django.urls import path

from .views import view_substack, add_to_substack

app_name = "substack"

urlpatterns = [
    path('substack/', view_substack, name='substack'),
    path("substack/add_to_substack/", add_to_substack, name="add_to_substack"),
]