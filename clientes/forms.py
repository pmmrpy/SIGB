__author__ = 'pmmr'

from django import forms
from clientes.models import Cliente, Reserva  # ClienteDocumento
from suit.widgets import SuitDateWidget
# from django.forms.extras.widgets import SelectDateWidget
# from django.contrib.admin.widgets import AdminDateWidget
# from django.forms.widgets import DateTimeInput
# from django.forms.widgets import DateInput
# from django.forms.widgets import SplitDateTimeWidget
# from functools import partial


# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

# class CalendarWidget(forms.TextInput):
#     class Media:
#         js = ('/static/clientes/js/datepicker.js')


class ClienteForm(forms.ModelForm):

    # Intento de implementacion del widget de Fecha de Django Suit
    class Meta:
        model = Cliente
        # fields = ('nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'direccion', 'pais', 'ciudad', 'email',
        # 'documentos')
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': SuitDateWidget,  # (attrs={'class': 'datepicker', 'changeMonth': 'true', 'changeYear': 'true'}),
            # 'fecha_nacimiento': SelectDateWidget,
            # 'fecha_nacimiento': SplitDateTimeWidget,
            # 'fecha_nacimiento': DateInput(attrs={'class': 'datepicker'}),
            # 'fecha_nacimiento': DateTimeInput(attrs={'type': 'date'})
            # 'fecha_nacimiento': AdminDateWidget(attrs={'changeMonth': 'true', 'changeYear': 'true'}),
            # 'fecha_nacimiento': CalendarWidget,
        }

    # def clean_telefono(self):
    #     dato = self.cleaned_data['telefono']
    #     if str(dato).startswith("595"):
    #         return dato
    #     else:
    #         raise forms.ValidationError("Numero de telefono incorrecto. Debe empezar por 595")


# class ClienteDocumentoForm(forms.ModelForm):
#     def clean(self):
#         datos = super(ClienteDocumentoForm, self).clean()
#
#         if 'tipo_documento' in self.cleaned_data and \
#            'numero_documento' in self.cleaned_data:
#             tipo = self.cleaned_data['tipo_documento']
#             cedula = self.cleaned_data['numero_documento']
#
#             documentos = ClienteDocumento.objects.filter(tipo_documento=tipo, numero_documento=cedula)
#             if len(documentos) > 0:
#                 raise forms.ValidationError("Ya existe un documento para el cliente " + documentos[0].cliente.nombres)
#             else:
#                 return datos
#         else:
#             return datos


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        localized_fields = ('pago',)
        widgets = {
            # 'nombres': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'apellidos': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'fecha_nacimiento': HTML5Input(input_type='date'),
            # 'salario': NumberInput(attrs={'localize': 'True'}),  # (attrs={'class': 'input-mini'}), # 'min': '1', 'max': '5'
        }