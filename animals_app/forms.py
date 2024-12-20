from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['target', 'kind', 'nickname', 'description', 'signs',
                  'city', 'phone_number',
                  'contact_people']
        widgets = {
            'target': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'kind': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'signs': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_people': forms.TextInput(attrs={'class': 'form-control'}),
        }
