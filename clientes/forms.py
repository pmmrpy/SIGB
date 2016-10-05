# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from bar.models import Documento

__author__ = 'pmmr'

from django import forms
from clientes.models import Cliente, Reserva, ClienteTelefono, ClienteDocumento  # ClienteDocumento
# from dal import autocomplete
# from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
# from suit.widgets import SuitDateWidget
# from django.forms.extras.widgets import SelectDateWidget
# from django.contrib.admin.widgets import AdminDateWidget
# from django.forms.widgets import DateTimeInput
# from django.forms.widgets import DateInput
# from django.forms.widgets import SplitDateTimeWidget
# from functools import partial
from datetimewidget.widgets import DateWidget
from dal import autocomplete
import re

ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'

# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

# class CalendarWidget(forms.TextInput):
#
#     class Media:
#         js = [
#             'clientes/js/datepicker.js'
#         ]

# BIRTH_YEAR_CHOICES = range(2012, 1920, -1)


# class DateInput(forms.DateInput):
#     input_type = 'date'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        # fields = ('nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'direccion', 'pais', 'ciudad', 'email',
        # 'documentos')
        fields = '__all__'
        widgets = {
            # Intento de implementacion del widget de Fecha de Django Suit
            # 'fecha_nacimiento': SuitDateWidget,
            # 'fecha_nacimiento': (attrs={'class': 'datepicker', 'changeMonth': 'true', 'changeYear': 'true'}),
            # 'fecha_nacimiento': SelectDateWidget(years=BIRTH_YEAR_CHOICES,
            #                                      empty_label=(u"Seleccione el Año", "Seleccione el Mes",
            #                                                   "Seleccione el Dia")),
            # 'fecha_nacimiento': SplitDateTimeWidget,
            # 'fecha_nacimiento': DateInput(),  # DateInput(attrs={'class': 'datepicker'}),
            # 'fecha_nacimiento': DateTimeInput(attrs={'type': 'date'})
            # 'fecha_nacimiento': AdminDateWidget(attrs={'changeMonth': True, 'changeYear': True}),
            # 'fecha_nacimiento': CalendarWidget,
            'fecha_nacimiento': DateWidget,
            'pais': autocomplete.ModelSelect2(url='bar:pais-autocomplete'),
            # 'ciudad': autocomplete.ModelSelect2(url='/bar/ciudad-autocomplete/'),
            'ciudad': autocomplete.ModelSelect2(url='bar:ciudad-autocomplete', forward=['pais']),
        }

    # def clean_telefono(self):
    #     dato = self.cleaned_data['telefono']
    #     if str(dato).startswith("595"):
    #         return dato
    #     else:
    #         raise forms.ValidationError("Numero de telefono incorrecto. Debe empezar por 595")


class ClienteTelefonoForm(forms.ModelForm):
    class Meta:
        model = ClienteTelefono
        fields = '__all__'
        widgets = {
            'codigo_pais_telefono': autocomplete.ModelSelect2(url='bar:codigo_pais_telefono-autocomplete'),
            'codigo_operadora_telefono': autocomplete.ModelSelect2(url='bar:codigo_operadora_telefono-autocomplete',
                                                                   forward=['codigo_pais_telefono']),
        }


class ClienteDocumentoForm(forms.ModelForm):
    class Meta:
        model = ClienteDocumento
        fields = '__all__'

    # def clean(self):
    #     datos = super(ClienteDocumentoForm, self).clean()
    #
    #     if 'tipo_documento' in self.cleaned_data and \
    #        'numero_documento' in self.cleaned_data:
    #         tipo = self.cleaned_data['tipo_documento']
    #         cedula = self.cleaned_data['numero_documento']
    #
    #         documentos = ClienteDocumento.objects.filter(tipo_documento=tipo, numero_documento=cedula)
    #         if len(documentos) > 0:
    #             raise forms.ValidationError("Ya existe un documento para el cliente " + documentos[0].cliente.nombres)
    #         else:
    #             return datos
    #     else:
    #         return datos

    def clean(self):
        super(ClienteDocumentoForm, self).clean()

        # import pdb
        # pdb.set_trace()

        data = self.cleaned_data

        # tipo_documento = cleaned_data.get("tipo_documento")

        # if not ('tipo_documento' in cleaned_data.keys() and 'numero_documento' in cleaned_data.keys()):
        #     raise ValidationError({
        #         'tipo_documento': _('Ingrese el dato del Tipo de Documento del Cliente.'),
        #         'numero_documento': _('Ingrese el dato del Numero de Documento del Cliente.'),
        #     })

        if ('tipo_documento' in data.keys()) and 'numero_documento' in data.keys() and \
                self.cleaned_data.get('tipo_documento') == Documento.objects.get(documento='RUC'):
            # numero_documento = self.numero_documento
            if not re.match(r'^[0-9]*$', self.cleaned_data.get('numero_documento')):
                raise ValidationError({'numero_documento': ('Solo se permiten caracteres numericos para el Tipo de '
                                                            'Documento RUC.')})


class ReservaForm(forms.ModelForm):

    # cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=autocomplete.ModelSelect2(url='cliente-autocomplete'))

    class Meta:
        model = Reserva
        fields = '__all__'
        localized_fields = ('pago',)
        widgets = {
            # 'cliente': autocomplete.ModelSelect2(url='cliente-autocomplete')
            # 'nombres': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'apellidos': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'fecha_nacimiento': HTML5Input(input_type='date'),
            # 'salario': NumberInput(attrs={'localize': 'True'}),  # (attrs={'class': 'input-mini'}), # 'min': '1', 'max': '5'
        }
        # cliente = AutoCompleteSelectField('clientes', required=True, help_text='Seleccione el Cliente para la Reserva.')