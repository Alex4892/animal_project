from django.urls import path

from .views import (add_animal_house_view)


app_name = "houses"

urlpatterns = [
    path('add_animal_house/', add_animal_house_view,
         name='add_animal_house'),
]
