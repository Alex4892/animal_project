from rest_framework import serializers
from animals_app.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'target', 'kind',
            'nickname', 'description',
            'signs', 'city',
            'phone_number', 'contact_people',
            'image', 'submit', 'create_at',
            'is_verified'
        ]
