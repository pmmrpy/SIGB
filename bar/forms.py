__author__ = 'pmmr'

from django import forms
from bar.models import Pais, Ciudad
from dal import autocomplete


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'


# class CiudadForm(forms.ModelForm):
#     class Meta:
#         model = Ciudad
#         fields = '__all__'
#         widgets = {
#             '':
#         }