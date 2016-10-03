import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.safestring import mark_safe
from bar.models import Caja
from compras.models import Empresa
from personal.models import Empleado

__author__ = 'pmmr'

from django import forms
from ventas.models import Pedido, PedidoDetalle, AperturaCaja, Venta

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'
ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'

    
class AperturaCajaForm(forms.ModelForm):

    # cajero2 = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Cajero')
    # horario2 = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario')
    
    class Meta:
        model = AperturaCaja
        fields = '__all__'
        # widgets = {
        #     'cajero': forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}),
        #                               label='Cajero', required=False),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(AperturaCajaForm, self).__init__(*args, **kwargs)
    # #
    # #     import pdb
    # #     pdb.set_trace()
    # #
    # #     # if self.instance:
    # #     usuario = Empleado.objects.get(usuario=self.request.user)
    # #     self.initial['cajero'] = usuario
    # #     self.initial['horario'] = usuario.horario.id
    # #     # self.fields['cajero'].widget.attrs['required'] = False
    # #     # self.fields['horario'].widget.attrs['required'] = False
    # #     # self.fields['cajero'].widget.attrs['readonly'] = True
    # #     # self.fields['horario'].widget.attrs['readonly'] = True
    #     self.fields['cajero'].widget.attrs['disabled'] = True
    #     self.fields['horario'].widget.attrs['disabled'] = True

    def clean(self):
        super(AperturaCajaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        # usuario = self.data.get('cajero', '')
        # print usuario

        apertura_caja = self.instance

        if apertura_caja:
            usuario = Empleado.objects.get(usuario=self.request.user)
            if usuario.cargo.cargo != 'CA':
                raise ValidationError({'cajero': 'El Usuario no posee el cargo de Cajero. Modifique el cargo del '
                                                 'Usuario y vuelva a intentarlo.'})

            aperturas = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja='VIG')
            if aperturas.exists():
                raise ValidationError({'cajero': 'El Cajero posee una Apertura de Caja vigente. Solo puede tener una '
                                                 'Caja abierta.'})

            caja = Caja.objects.get(pk=self.data.get('caja'))
            if caja.estado_caja == 'ABI':
                raise ValidationError({'caja': 'La Caja seleccionada se encuentra con estado ABIERTO.'})

        #     return apertura_caja.
        # else:
        #     return self.cleaned_data['cajero', 'horario']


class PedidoDetalleInlineForm(forms.ModelForm):

    anulado = forms.BooleanField(label='Anular?', required=False)

    class Meta:
        model = PedidoDetalle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoDetalleInlineForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        detalle_pedido = self.instance

        if detalle_pedido.pk and detalle_pedido.procesado is True:  # self.request.method == 'GET' and
            self.fields['producto_pedido'].widget.attrs['required'] = False
            self.fields['producto_pedido'].widget.attrs['readonly'] = True
            self.fields['producto_pedido'].widget.attrs['disabled'] = True
            self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
            # self.fields['procesado'].widget.attrs['readonly'] = True
            self.fields['anulado'].widget.attrs['disabled'] = True
        # elif detalle_pedido.pk and detalle_pedido.procesado is False and detalle_pedido.anulado is True:  # self.request.method == 'GET' and
        #     self.fields['producto_pedido'].widget.attrs['required'] = False
        #     self.fields['producto_pedido'].widget.attrs['readonly'] = True
        #     # self.fields['producto_pedido'].widget.attrs['disabled'] = True
        #     self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
        #     # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
        #     self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
        #     # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
        #     self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
        #     # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
        #     # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
        #     # self.fields['procesado'].widget.attrs['readonly'] = True
        #     self.fields['anulado'].widget.attrs['readonly'] = True
        #     self.fields['anulado'].widget.attrs['disabled'] = True


class PedidoForm(forms.ModelForm):
    id_cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='ID Cliente', required=False)
    cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Nombre Cliente', required=False)
    monto_entrega_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Monto Entrega Reserva', required=False, initial=0)

    total_pedido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                   label=mark_safe('<strong style="font-size: 20px;">Total Pedido</strong>'),
                                   required=False, initial=0)

    class Meta:
        model = Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        pedido = self.instance

        if pedido.pk:
            self.initial['id_cliente_reserva'] = pedido.reserva.cliente.id
            self.initial['cliente_reserva'] = pedido.reserva.cliente.nombre_completo
            self.initial['monto_entrega_reserva'] = pedido.reserva.pago


class VentaForm(forms.ModelForm):
    timbrado = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Timbrado', required=False)
    fecha_limite_vigencia_timbrado = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha Vigencia Timbrado', required=False)
    caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Caja', required=False)
    cajero = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Cajero', required=False)
    horario = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario', required=False)
    fecha_apertura_caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha Apertura', required=False)

    total_pedido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                   label=mark_safe('<strong style="font-size: 14px;">Total Pedido</strong>'),
                                   required=False, initial=0)

    posee_reserva = forms.BooleanField(label='Posee reserva?', required=False)
    entrega_reserva = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                      label=mark_safe('<strong style="font-size: 14px;">Monto Entrega Reserva</strong>'),
                                      required=False, initial=0)

    total_venta = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                  label=mark_safe('<strong style="font-size: 20px;">Total Venta</strong>'),
                                  required=False, initial=0)
    
    class Meta:
        model = Venta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)

    # def is_valid(self):
    #     super(VentaForm, self).is_valid()

        # import pdb
        # pdb.set_trace()

        # empresa = Empresa.objects.get(pk=self.data.get('empresa', ''))
        empresa = self.instance.empresa
        # if empresa.timbrado.estado_timbrado == 'IN':
        #     # raise forms.ValidationError({'timbrado': 'El Timbrado esta inactivo. Verifique los datos de la Empresa.'})
        #     raise forms.ValidationError('El Timbrado esta inactivo. Verifique los datos de la Empresa.')
        # elif empresa.timbrado.fecha_limite_vigencia_timbrado < timezone.now().date():
        #     # raise ValidationError({'timbrado': 'El Timbrado esta vencido. Verifique los datos de la Empresa.'})
        #     raise ('El Timbrado esta vencido. Verifique los datos de la Empresa.')
        # else:
        self.initial['timbrado'] = empresa.timbrado.timbrado
        self.initial['fecha_limite_vigencia_timbrado'] = datetime.datetime.strftime(empresa.timbrado.fecha_limite_vigencia_timbrado, '%d/%m/%Y')

        usuario = Empleado.objects.get(usuario=self.request.user)
        apertura = AperturaCaja.objects.get(cajero=usuario, estado_apertura_caja='VIG')
        # if apertura is None:
        #     # raise ValidationError({'apertura_caja': 'El Cajero NO posee una Apertura de Caja vigente. Realice una '
        #     #                                         'Apertura de Caja para poder registrar ventas.'})
        #     raise ('El Cajero NO posee una Apertura de Caja vigente. Realice una Apertura de Caja para poder '
        #            'registrar ventas.')
        # else:
        self.initial['apertura_caja'] = apertura.id
        self.initial['cajero'] = apertura.cajero
        self.initial['caja'] = apertura.caja
        self.initial['horario'] = apertura.horario
        self.initial['fecha_apertura_caja'] = datetime.datetime.strftime(apertura.fecha_apertura_caja, '%d/%m/%Y')
        # self.fields['apertura_caja'].widget.attrs['readonly'] = True
        # self.fields['apertura_caja'].widget.attrs['disabled'] = True

    def clean(self):
        super(VentaForm, self).clean()

        # empresa = Empresa.objects.get(pk=self.data.get('empresa', ''))
        empresa = self.instance.empresa
        if empresa.timbrado.estado_timbrado == 'IN':
            raise forms.ValidationError({'timbrado': 'El Timbrado esta inactivo. Verifique los datos de la Empresa.'})
            # raise forms.ValidationError('El Timbrado esta inactivo. Verifique los datos de la Empresa.')
        elif empresa.timbrado.fecha_limite_vigencia_timbrado < timezone.now().date():
            raise ValidationError({'timbrado': 'El Timbrado esta vencido. Verifique los datos de la Empresa.'})
            # raise ('El Timbrado esta vencido. Verifique los datos de la Empresa.')
        # else:
        #     self.initial['timbrado'] = empresa.timbrado.timbrado
        #     self.initial['fecha_limite_vigencia_timbrado'] = datetime.datetime.strftime(empresa.timbrado.fecha_limite_vigencia_timbrado, '%d/%m/%Y')

        usuario = Empleado.objects.get(usuario=self.request.user)
        apertura = AperturaCaja.objects.get(cajero=usuario, estado_apertura_caja='VIG')
        if apertura is None:
            raise ValidationError({'apertura_caja': 'El Cajero NO posee una Apertura de Caja vigente. Realice una '
                                                    'Apertura de Caja para poder registrar ventas.'})
            # raise ('El Cajero NO posee una Apertura de Caja vigente. Realice una Apertura de Caja para poder '
            #        'registrar ventas.')
        # else:
        #     self.initial['apertura_caja'] = apertura.id
        #     self.initial['cajero'] = apertura.caja
        #     self.initial['caja'] = apertura.cajero
        #     self.initial['horario'] = apertura.horario
        #     self.fields['apertura_caja'].widget.attrs['readonly'] = True
        #     self.fields['apertura_caja'].widget.attrs['disabled'] = True