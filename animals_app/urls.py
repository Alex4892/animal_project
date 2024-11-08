from django.urls import path

from .views import (view_animals, view_detail_animal, add_animal_view,
                    delete_animal_view, edit_animal_view, change_animal_status)


app_name = "animals"

urlpatterns = [
    path('', view_animals, name='index'),
    path('detail_animal/<int:animal_id>/',
         view_detail_animal, name='detail_animal'),
    path('add_animal/', add_animal_view, name='add_animal'),
    path('edit_animal/<int:animal_id>/', edit_animal_view, name='edit_animal'),
    path('delete_animal/<int:animal_id>/',
         delete_animal_view, name='delete_animal'),
    path('change-animal-status/<int:animal_id>/',
         change_animal_status, name='change_animal_status'),
]
