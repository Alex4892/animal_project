from django.urls import path

from .views import view_substack, add_to_substack, remove_from_substack

app_name = "substack"

urlpatterns = [
    path('substack/', view_substack, name='substack'),
    path("substack/add_to_substack/", add_to_substack, name="add_to_substack"),
    path('substack/remove_from_substack/', remove_from_substack,
         name='remove_from_substack'),
]
