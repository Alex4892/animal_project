from django import forms
from .models import Clinic


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name_clinic', 'adress', 'cite']
        widgets = {
            'name_clinic': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'cite': forms.TextInput(attrs={'class': 'form-control'}),
        }
