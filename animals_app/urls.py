from django.urls import path

from .views import view_animals


app_name = "animals"

urlpatterns = [
    path('', view_animals, name='index')
]
