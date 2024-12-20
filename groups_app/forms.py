from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name_group', 'link_vk', 'cite']
        widgets = {
            'name_group': forms.TextInput(attrs={'class': 'form-control'}),
            'link_vk': forms.TextInput(attrs={'class': 'form-control'}),
            'cite': forms.TextInput(attrs={'class': 'form-control'}),
        }
