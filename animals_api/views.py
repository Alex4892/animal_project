from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from animals_app.models import Animal
from .serializers import AnimalSerializer

@api_view(['GET'])
def animal_list(request):
    animals = Animal.objects.all()
    if not animals.exists():
        return Response(
            {"detail": "No animals found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def animal_detail(request, pk):
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return Response(
            {"detail": "Объявление не найдено."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = AnimalSerializer(animal)
    return Response(serializer.data)

# Create your views here.
