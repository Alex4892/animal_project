from django.urls import path

from .views import animal_list, animal_detail


app_name = "animals_api"

urlpatterns = [
    path('animals/', animal_list, name='animal_list'),
    path('animal/<int:pk>/detail/', animal_detail, name='animal_detail')
]
