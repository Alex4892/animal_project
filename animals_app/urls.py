from django.urls import path

from .views import view_animals, view_detail_animal


app_name = "animals"

urlpatterns = [
    path('', view_animals, name='index'),
    path('detail_animal/<int:animal_id>/', view_detail_animal, name='detail_animal')
]
