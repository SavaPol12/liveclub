from .models import note
from django.forms import ModelForm, TextInput, Textarea


class noteForm(ModelForm):
    class Meta:
        model = note
        fields = ["person_do_it", "title", "note"]
        widgets = {
            "person_do_it": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя(никнейм)'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "note": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите запись'
            }),
        }