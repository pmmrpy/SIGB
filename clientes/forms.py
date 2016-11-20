# -*- coding: utf-8 -*-

__author__ = 'pmmr'

import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from bar.models import Documento, Mesa
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
from django.views.generic.dates import timezone_today

ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'


def calcular_dv(numero, base=11):
    total = 0
    k = 2
    for i in range(len(numero) - 1, - 1, - 1):
        k = 2 if k > base else k
        total += int(numero[i]) * k
        k += 1
    resto = total % 11
    return (11 - resto) if resto > 1 else 0

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

    # def __init__(self, *args, **kwargs):
    #     super(ClienteForm, self).__init__(*args, **kwargs)
    #
    #     import pdb
    #     pdb.set_trace()


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
    # doc_ruc_cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Doc. Cliente Reserva', required=False)
    cliente_documento_reserva = forms.CharField(widget=forms.Select(attrs={'class':'hidden'}), label='Documento', required=False)
    # cliente_documento_factura = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'hidden'}), queryset=ClienteDocumento.objects.all, label='Documento', required=False)
    direccion_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Direccion', required=False)
    pais_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Pais', required=False)
    ciudad_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Ciudad', required=False)
    telefonos_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 500px;'}), label='Telefonos', required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Email', required=False)

    class Meta:
        model = Reserva
        fields = '__all__'
        # localized_fields = ('pago',)
        widgets = {
            # 'cliente': autocomplete.ModelSelect2(url='cliente-autocomplete')
            # 'nombres': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'apellidos': HTML5Input(attrs={'autocomplete': 'off'}),
            # 'fecha_nacimiento': HTML5Input(input_type='date'),
            # 'salario': NumberInput(attrs={'localize': 'True'}),  # (attrs={'class': 'input-mini'}), # 'min': '1', 'max': '5'
        }
        # cliente = AutoCompleteSelectField('clientes', required=True, help_text='Seleccione el Cliente para la Reserva.')

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        reserva = self.instance

        if reserva.pk:

            documentos = []
            for o in reserva.cliente.clientedocumento_set.all():
                if o.tipo_documento.documento == 'RUC':
                    documentos.append((('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11)))), ('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11))))),)
                else:
                    documentos.append((('%s: %s' % (o.tipo_documento.documento, o.numero_documento)), ('%s: %s' % (o.tipo_documento.documento, o.numero_documento))),)

            # documentos = []
            # for o in reserva.cliente.clientedocumento_set.all():
            #     if o.tipo_documento.documento == 'RUC':
            #         documentos.append((('%s-%s' % (o.numero_documento, str(calcular_dv(o.numero_documento, 11)))), ('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11))))),)
            #     else:
            #         documentos.append((('%s' % o.numero_documento), ('%s: %s' % (o.tipo_documento.documento, o.numero_documento))),)

            # print self.fields['sexo'].choices
            self.fields['cliente_documento_reserva'] = forms.ChoiceField(choices=documentos, required=False, label='Documento', initial=reserva.cliente_documento_reserva)
            # self.fields['cliente_documento_reserva'].widget.attrs['readonly'] = True
            # self.fields['cliente_documento_reserva'].widget.attrs['disabled'] = True
            self.initial['direccion_cliente'] = reserva.cliente.direccion
            self.initial['pais_cliente'] = reserva.cliente.pais
            self.initial['ciudad_cliente'] = reserva.cliente.ciudad
            self.initial['telefonos_cliente'] = " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=reserva.cliente.pk)])
            self.initial['email'] = reserva.cliente.email

    def clean(self):
        cleaned_data = super(ReservaForm, self).clean()

        # 25/10/2016:
        # * VALIDACIONES:
        # 1) Se pueden realizar Reservas de Mesas desde las 18 hasta las 21 hs, pasada las 21 hs se deben liberar las
        # Mesas Reservadas y cambiar el Estado de la Reserva a CADUCADA.
        # 2) Una Mesa puede ser reservada solo una vez por jornada.
        # 3) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.

        # import pdb
        # pdb.set_trace()

        reserva = self.instance

        if self.cleaned_data['cliente_documento_reserva'] == '':
            raise ValidationError({'cliente_documento_reserva': 'Debe seleccionar un documento del Cliente para '
                                                                'registrar la Reserva.'})

        # ==========================================================================================================
        # Validar que las Mesas seleccionadas NO tengan estado "IN"
        # ==========================================================================================================
        # if reserva.pk:
        #     mesas_guardadas = reserva.mesas_set.all()
        # else:
        #     mesas_guardadas = None

        # mesa = self.data.get('mesa_pedido', None)
        # if mesa is not None:
        #     mesa_elegida = Mesa.objects.get(pk=mesa)
        # else:
        #     mesa_elegida = None

        try:
            for mesa_elegida in self.cleaned_data['mesas']:
                # if mesa_elegida is not None and mesas_guardadas is None or \
                #                                 mesa_elegida is not None and mesas_guardadas is not None and mesa_elegida not in mesas_guardadas:
                if mesa_elegida.estado.mesa_estado == 'IN':
                    raise ValidationError({'mesas': '%s se encuentra inactiva. Seleccione otra Mesa.' % mesa_elegida})
                # elif mesa_elegida.estado.mesa_estado == 'OC':
                #     raise ValidationError({'mesa_pedido': '%s ya se encuentra ocupada. Seleccione otra Mesa.' % mesa_elegida})

        except KeyError:
            pass

        # ==========================================================================================================
        # Validar que las Mesas seleccionadas no esten Reservadas
        # Tener en cuenta que las Reservas se pueden realizar y usufructuar entre las 18:00 y 21:00 hs
        # ==========================================================================================================
        # fecha = timezone.make_aware(reserva.fecha_hora_reserva, timezone.get_default_timezone())
        # fecha = timezone_today()
        # from_date = datetime.datetime.combine(fecha, datetime.time.min).replace(tzinfo=timezone.utc)
        # to_date = datetime.datetime.combine(fecha, datetime.time.max).replace(tzinfo=timezone.utc)

        # reservas = Reserva.objects.filter(fecha_hora_reserva__range=(from_date, to_date))

        reservas = Reserva.objects.filter(fecha_hora_reserva__year=self.cleaned_data['fecha_hora_reserva'].year,
                                          fecha_hora_reserva__month=self.cleaned_data['fecha_hora_reserva'].month,
                                          fecha_hora_reserva__day=self.cleaned_data['fecha_hora_reserva'].day,
                                          estado__reserva_estado='VIG')

        if reserva.pk:
            reservas = reservas.exclude(id=reserva.pk)

        for reserva_fecha in reservas:
            mesas_reservadas = reserva_fecha.mesas.all()

            # mesa = self.data.get('mesas', None)
            # if mesa is not None:
            #     mesa_elegida = Mesa.objects.get(pk=mesa)
            # else:
            #     mesa_elegida = None
            try:
                for mesa_elegida in self.cleaned_data['mesas']:
                    # Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
                    if mesa_elegida is not None and mesas_reservadas is not None and mesa_elegida in mesas_reservadas:
                        raise ValidationError({'mesas': '%s ya se encuentra reservada para la fecha indicada. Seleccione '
                                                        'otra Mesa.' % mesa_elegida})
            except KeyError:
                pass

        return cleaned_data