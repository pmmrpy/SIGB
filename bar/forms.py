__author__ = 'pmmr'

from django import forms
from bar.models import Pais


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'