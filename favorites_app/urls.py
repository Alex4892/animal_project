from django.urls import path

from .views import view_favorite, add_to_favorite, remove_from_favorite

app_name = "favorite"

urlpatterns = [
    path('favorite/', view_favorite, name='favorite'),
    path("favorite/add_to_favorite/", add_to_favorite, name="add_to_favorite"),
    path('favorite/remove_from_favorite/', remove_from_favorite,
         name='remove_from_favorite'),
]
