__author__ = 'pmmr'

from django import forms
from bar.models import Pais, Ciudad, Timbrado
from django.core.validators import RegexValidator
from dal import autocomplete

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'
ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'


class TimbradoForm(forms.ModelForm):
    timbrado = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO), max_length=8, label='Numero de Timbrado')
    
    class Meta:
        model = Timbrado
        fields = '__all__'
    
# class CiudadForm(forms.ModelForm):
#     class Meta:
#         model = Ciudad
#         fields = '__all__'
#         widgets = {
#             '':
#         }