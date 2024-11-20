from django import forms
from .models import Clinic
# from .models import House


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name_clinic', 'adress']
        widgets = {
            'name_clinic': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
        }