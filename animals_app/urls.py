from django.urls import path

from .views import view_animals, view_detail_animal, add_animal, delete_animal, edit_animal


app_name = "animals"

urlpatterns = [
    path('', view_animals, name='index'),
    path('detail_animal/<int:animal_id>/', view_detail_animal, name='detail_animal'),
    path('add_animal/', add_animal, name='add_animal'),
    path('edit_animal/<int:animal_id>/', edit_animal, name='edit_animal'),
    path('delete_animal/<int:animal_id>/', delete_animal, name='delete_animal')
]
