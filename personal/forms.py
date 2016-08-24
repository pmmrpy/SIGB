__author__ = 'pmmr'

from django import forms
from personal.models import Empleado, EmpleadoTelefono
# from suit.widgets import NumberInput
# from suit.widgets import HTML5Input
# from django.forms.widgets import TextInput
# from django.contrib import humanize
from datetimewidget.widgets import DateWidget


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        localized_fields = ('salario',)
        widgets = {
            # 'nombres': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'apellidos': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'fecha_nacimiento': HTML5Input(input_type='date'),
            # 'salario': NumberInput,  #(attrs={'localize': 'True'}),  # (attrs={'class': 'input-mini'}), # 'min': '1', 'max': '5'
            # 'salario': HTML5Input(input_type='number')
            'fecha_nacimiento': DateWidget,
        }


class EmpleadoTelefonoForm(forms.ModelForm):
    class Meta:
        model = EmpleadoTelefono
        fields = '__all__'
        widgets = {
            # 'telefono': HTML5Input(input_type='tel')
        }