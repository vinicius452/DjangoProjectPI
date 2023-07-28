from django import forms

from .models import Celular


class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = '__all__'