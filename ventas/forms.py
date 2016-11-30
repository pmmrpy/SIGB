import datetime
from django.contrib.admin.sites import site
from dal import autocomplete, widgets
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import RegexValidator
from django.db.models.query_utils import Q
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import BaseInlineFormSet
from django.forms.widgets import DateTimeInput
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets
from bar.models import Caja, Mesa, Sector, Deposito
from clientes.models import ClienteDocumento, Reserva, ClienteTelefono
from compras.models import Empresa
from personal.models import Empleado
from stock.models import StockDepositoAjusteInventario, ProductoCompuestoDetalle, Producto
from ventas.customwidgets import ReadOnlySelect

__author__ = 'pmmr'

from django import forms
from ventas.models import Pedido, PedidoDetalle, AperturaCaja, Venta, InicioJornada, FinJornada, CierreCaja, \
    VentaDetalle

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}

ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'

ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'

ATTR_NUMERICO_RO_RESALTADO_3 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_3['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: green;'

ATTR_NUMERICO_RO_monto_registro = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_monto_registro['style'] += 'width: 150px;'

ATTR_NUMERICO_monto_rendicion = ATTR_NUMERICO.copy()
ATTR_NUMERICO_monto_rendicion['style'] += 'width: 150px;'

ATTR_NUMERICO_RO_monto_apertura = ATTR_NUMERICO_RO_RESALTADO_2.copy()
ATTR_NUMERICO_RO_monto_apertura['style'] += 'width: 150px;'

ATTR_NUMERICO_RO_total_efectivo = ATTR_NUMERICO_RO_RESALTADO_2.copy()
ATTR_NUMERICO_RO_total_efectivo['style'] += 'width: 150px;'

ATTR_NUMERICO_RO_cant_oper = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_cant_oper['style'] += 'width: 50px;'

# ATTR_NUMERICO_RO_monto_diferencia = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_monto_diferencia = {'style': 'text-align:right; width: 150px; font-size: 14px; font-weight: bold; color: red;', 'class': 'diferencia', 'data-a-sep': '.', 'data-a-dec': ',',
                                     'type': 'number', 'readonly': 'readonly'}


def calcular_dv(numero, base=11):
    total = 0
    k = 2
    for i in range(len(numero) - 1, - 1, - 1):
        k = 2 if k > base else k
        total += int(numero[i]) * k
        k += 1
    resto = total % 11
    return (11 - resto) if resto > 1 else 0


class PedidoDetalleFormSet(BaseInlineFormSet):

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request
        for form in self.forms:
            form.request = request


class PedidoDetalleInlineForm(forms.ModelForm):

    # cancelado = forms.BooleanField(label='Cancelar?', required=False)

    class Meta:
        model = PedidoDetalle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoDetalleInlineForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        detalle_pedido = self.instance
        if not detalle_pedido.pk:
            # self.fields['producto_pedido'].widget.attrs['required'] = False
            # self.fields['producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
            # self.fields['procesado'].widget.attrs['readonly'] = True
            self.initial['cancelado'] = False
            # self.fields['cancelado'].widget.attrs['readonly'] = True
            # self.fields['cancelado'].widget.attrs['disabled'] = True
            # self.fields['cancelado'].widget.attrs['style'] = 'display:none;'
        elif detalle_pedido.pk and detalle_pedido.procesado is True \
                and detalle_pedido.pedido.estado_pedido.pedido_estado == 'VIG' and detalle_pedido.pedido.jornada.estado_jornada == 'VIG':  # self.request.method == 'GET' and
            self.fields['producto_pedido'].widget.attrs['required'] = False
            self.fields['producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['producto_pedido'].widget.attrs['disabled'] = True
            self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
            # self.fields['procesado'].widget.attrs['readonly'] = True
            self.fields['cancelado'].widget.attrs['readonly'] = True
            self.fields['cancelado'].widget.attrs['disabled'] = True
            # self.fields['cancelado'].widget.attrs['style'] = 'display:none;'
        elif detalle_pedido.pk and detalle_pedido.procesado is False and detalle_pedido.cancelado is True \
                and detalle_pedido.pedido.estado_pedido.pedido_estado == 'VIG' and detalle_pedido.pedido.jornada.estado_jornada == 'VIG':  # self.request.method == 'GET' and
            self.fields['producto_pedido'].widget.attrs['required'] = False
            self.fields['producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['producto_pedido'].widget.attrs['disabled'] = True
            self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
            # self.fields['procesado'].widget.attrs['readonly'] = True
            self.fields['cancelado'].widget.attrs['readonly'] = True
            self.fields['cancelado'].widget.attrs['disabled'] = True
            # self.fields['cancelado'].widget.attrs['style'] = 'display:none;'
        elif detalle_pedido.pk and detalle_pedido.procesado is False and detalle_pedido.cancelado is False \
                and detalle_pedido.pedido.estado_pedido.pedido_estado == 'VIG' and detalle_pedido.pedido.jornada.estado_jornada == 'VIG':  # self.request.method == 'GET' and
            self.fields['producto_pedido'].widget.attrs['required'] = False
            self.fields['producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['producto_pedido'].widget.attrs['disabled'] = True
            self.fields['precio_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['precio_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['cantidad_producto_pedido'].widget.attrs['disabled'] = True
            self.fields['total_producto_pedido'].widget.attrs['readonly'] = True
            # self.fields['total_producto_pedido'].widget.attrs['disabled'] = True
            # self.fields['fecha_pedido_detalle'].widget.attrs['readonly'] = True
            # self.fields['procesado'].widget.attrs['readonly'] = True
            # self.fields['cancelado'].widget.attrs['readonly'] = True
            # self.fields['cancelado'].widget.attrs['disabled'] = True
            # self.fields['cancelado'].widget.attrs['style'] = 'display:none;'

    def clean_cancelado(self):

        # import pdb
        # pdb.set_trace()

        detalle_pedido = self.instance
        if detalle_pedido.pk and detalle_pedido.procesado is True or detalle_pedido.pk \
                and detalle_pedido.procesado is False and detalle_pedido.cancelado is True:
            return self.instance.cancelado
        else:
            return self.cleaned_data['cancelado']

    def clean(self):
        cleaned_data = super(PedidoDetalleInlineForm, self).clean()

        # import pdb
        # pdb.set_trace()

        detalle_pedido = self.instance
        jornada = InicioJornada.objects.none
        if hasattr(detalle_pedido, 'pedido') is False:
            if self.data.get('jornada') != '':
                jornada = InicioJornada.objects.get(pk=self.data.get('jornada'))
            else:
                # raise ValidationError({'jornada': 'El Mozo/Barman NO posee una Jornada vigente. Realice un Inicio '
                #                                   'de Jornada para registrar pedidos.'})
                pass

        elif detalle_pedido.pk or not detalle_pedido.pk and detalle_pedido.pedido.pk:
            jornada = InicioJornada.objects.get(pk=detalle_pedido.pedido.jornada.id)
        # elif not detalle_pedido.pk and detalle_pedido.pedido.pk:
        #     jornada = InicioJornada.objects.get(pk=self.data.get('jornada'))

        if "_continue" in self.request.POST or "_save" in self.request.POST:
            # Validar la Cantidad Existente del Producto seleccionado
            # Si el detalle_pedido aun no fue guardado realiza las siguientes validaciones:
            if not detalle_pedido.pk:
                if 'producto_pedido' not in self.cleaned_data:
                    raise ValidationError({'producto_pedido': 'Debe seleccionar un Producto.'})

                elif self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and self.cleaned_data['producto_pedido'].get_cantidad_existente_producto() <= 0:
                    if self.cleaned_data['producto_pedido'].compuesto is False:
                        raise ValidationError({'producto_pedido': 'El Producto seleccionado no posee stock disponible. '
                                                                  'Seleccione otro Producto.'})
                    elif self.cleaned_data['producto_pedido'].compuesto is True:
                        raise ValidationError({'producto_pedido': 'El Producto Compuesto seleccionado no posee stock '
                                                                  'disponible en todos o algunos de sus insumos. '
                                                                  'Seleccione otro Producto.'})

                # Verificar disponible en Deposito del Sector
                elif self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and self.cleaned_data['producto_pedido'].compuesto is False:
                    try:
                        producto_por_deposito = StockDepositoAjusteInventario.objects.get(id=self.cleaned_data['producto_pedido'].id, deposito_id=jornada.sector.deposito.id)
                        if producto_por_deposito.cantidad_existente <= 0:
                            raise ValidationError({'producto_pedido': 'El Producto seleccionado no posee stock disponible '
                                                                     'en el "%s" de su sector "%s". Verifique con el Encargado de '
                                                                     'Deposito de su sector.' % (jornada.sector.deposito, jornada.sector)})
                        elif self.cleaned_data['cantidad_producto_pedido'] > producto_por_deposito.cantidad_existente:
                            # self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = False  # ==> PROBAR: No debe ser necesario habilitar esta funcionalidad ya que al ser guardado un Pedido ya se descontaran los Productos solicitados sean Compuestos o por Unidad del Stock.
                            raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto '
                                                                              'seleccionado supera el stock disponible en el "%s" de su sector "%s". '
                                                                              'Modifique la cantidad solicitada o cancele '
                                                                              'el pedido de este Producto.' % (jornada.sector.deposito, jornada.sector)})
                    except StockDepositoAjusteInventario.DoesNotExist:
                        raise ValidationError({'producto_pedido': 'El Producto seleccionado no posee stock disponible en '
                                                                 'el "%s" de su sector "%s". Verifique con el Encargado de Deposito '
                                                                 'de su sector.' % (jornada.sector.deposito, jornada.sector)})

                elif self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and self.cleaned_data['producto_pedido'].compuesto is True:
                    # Si el ProductoCompuesto es una COMIDA se debe verificar la disponibilidad de los Insumos en el Deposito de la Cocina
                    if self.cleaned_data['producto_pedido'].categoria.categoria == 'CO':
                        deposito = Deposito.objects.get(deposito='DCO')
                        ingredientes = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=self.cleaned_data['producto_pedido'].pk)
                        cantidad = 0
                        for ingrediente in ingredientes:
                            if ingrediente.insumo.get_cantidad_existente_insumo_dco() > 0:
                                cant_posible_elaborar = ingrediente.insumo.get_cantidad_existente_insumo_dco() / (ingrediente.cantidad_insumo if ingrediente.cantidad_insumo else 1)

                                if ingrediente == ingredientes.first():
                                    cantidad = cant_posible_elaborar

                                elif cant_posible_elaborar < cantidad:
                                    cantidad = cant_posible_elaborar

                            elif ingrediente.insumo.get_cantidad_existente_insumo() <= 0:
                                cantidad = 0

                        if cantidad <= 0:
                            raise ValidationError({'producto_pedido': 'El Producto Compuesto (Comida) seleccionado no posee stock '
                                                                     'disponible en el %s. Verifique con el Encargado de '
                                                                     'este Deposito.' % deposito})
                        elif self.cleaned_data['cantidad_producto_pedido'] > cantidad:
                            # self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False  # ==> PROBAR: No debe ser necesario habilitar esta funcionalidad ya que al ser guardado un Pedido ya se descontaran los Productos solicitados sean Compuestos o por Unidad del Stock.
                            raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto Compuesto (Comida)'
                                                                              'seleccionado supera el stock disponible en el "%s". '
                                                                              'Modifique la cantidad solicitada o cancele '
                                                                              'el pedido de este Producto.' % deposito})

                    # Si el ProductoCompuesto es una BEBIDA se debe verificar la disponibilidad de los Insumos en el Deposito del Sector desde donde se realiza el Pedido o VentaOcasional
                    elif self.cleaned_data['producto_pedido'].categoria.categoria == 'BE':
                        # deposito = str(detalle_venta.venta.apertura_caja.sector.deposito.deposito)
                        # deposito = deposito.lower()
                        deposito = jornada.sector.deposito
                        det_prod_compuesto = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=self.cleaned_data['producto_pedido'].pk)
                        cantidad = 0

                        # Verifica la Cantidad Existente de cada Insumo para el Deposito desde donde se esta registrando el Pedido.
                        for insumo in det_prod_compuesto:
                            productos = Producto.objects.filter(insumo_id=insumo.insumo.id, tipo_producto='IN')
                            cant_existente = 0

                            for producto in productos:
                                try:
                                    prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                    cant_existente += prod_exist_deposito.cantidad_existente
                                except StockDepositoAjusteInventario.DoesNotExist:
                                    pass

                            if cant_existente > 0:
                                cant_posible_elaborar = cant_existente / (insumo.cantidad_insumo if insumo.cantidad_insumo else 1)

                                if insumo == det_prod_compuesto.first():
                                    cantidad = cant_posible_elaborar

                                elif cant_posible_elaborar < cantidad:
                                    cantidad = cant_posible_elaborar

                            elif cant_existente <= 0:
                                cantidad = 0

                        if cantidad <= 0:
                            raise ValidationError({'producto_pedido': 'El Producto Compuesto (Bebida) seleccionado no posee stock '
                                                                     'disponible en el "%s". Verifique con el Encargado de '
                                                                     'este Deposito.' % deposito})
                        elif self.cleaned_data['cantidad_producto_pedido'] > cantidad:
                            # self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False
                            raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto Compuesto (Bebida) '
                                                                              'seleccionado supera el stock disponible en el "%s". '
                                                                              'Modifique la cantidad solicitada o cancele '
                                                                              'el pedido de este Producto.' % deposito})
        # # ======================================================================================================================
        # # 24/11/2016: Como al momento de guardar el PedidoDetalle ya se realizan las validaciones sobre la
        # # disponibilidad en el Stock no se requieren realizar validaciones sobre el PedidoDetalle ya guardado (con
        # # detalle_pedido.pk ya asignado) por lo tanto se comenta este bloque de codigo.
        #     # Si el detalle_pedido YA fue guardado realiza las siguientes validaciones:
        #     elif detalle_pedido.pk:
        #         if self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and detalle_pedido.producto_pedido.get_cantidad_existente_producto() <= 0:
        #             if detalle_pedido.producto_pedido.compuesto is False:
        #                 raise ValidationError('El Producto seleccionado no posee stock disponible. Seleccione otro '
        #                                       'Producto.')
        #             elif detalle_pedido.producto_pedido.compuesto is True:
        #                 raise ValidationError('El Producto Compuesto seleccionado no posee stock disponible en todos o '
        #                                       'algunos de sus insumos. Seleccione otro Producto.')
        #
        #         # Verificar disponible en Deposito del Sector
        #         elif self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and detalle_pedido.producto_pedido.compuesto is False:
        #             try:
        #                 producto_por_deposito = StockDepositoAjusteInventario.objects.get(id=detalle_pedido.producto_pedido.id, deposito_id=jornada.sector.deposito.id)
        #                 if producto_por_deposito.cantidad_existente <= 0:
        #                     raise ValidationError('El Producto seleccionado no posee stock disponible en el %s de su '
        #                                           '%s. Verifique con el Encargado de Deposito de su sector.' % (jornada.sector.deposito, jornada.sector))
        #                 elif detalle_pedido.cantidad_producto_pedido > producto_por_deposito.cantidad_existente:
        #                     self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = False
        #                     raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto '
        #                                                                       'seleccionado supera el stock disponible. '
        #                                                                       'Modifique la cantidad solicitada o cancele '
        #                                                                       'el pedido de este Producto.'})
        #             except StockDepositoAjusteInventario.DoesNotExist:
        #                 raise ValidationError('El Producto seleccionado no posee stock disponible en el %s de su %s. '
        #                                       'Verifique con el Encargado de Deposito de su sector.' % (jornada.sector.deposito, jornada.sector))
        #
        #         elif self.cleaned_data['cancelado'] is False and detalle_pedido.procesado is False and detalle_pedido.producto_pedido.compuesto is True:
        #             # Si el ProductoCompuesto es una COMIDA se debe verificar la disponibilidad de los Insumos en el Deposito de la Cocina
        #             if detalle_pedido.producto_pedido.categoria.categoria == 'CO':
        #                 deposito = Deposito.objects.get(deposito='DCO')
        #                 ingredientes = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=detalle_pedido.producto_pedido.pk)
        #                 cantidad = 0
        #                 for ingrediente in ingredientes:
        #                     if ingrediente.insumo.get_cantidad_existente_insumo_dco() > 0:
        #                         cant_posible_elaborar = ingrediente.insumo.get_cantidad_existente_insumo_dco() / (ingrediente.cantidad_insumo if ingrediente.cantidad_insumo else 1)
        #
        #                         if ingrediente == ingredientes.first():
        #                             cantidad = cant_posible_elaborar
        #
        #                         elif cant_posible_elaborar < cantidad:
        #                             cantidad = cant_posible_elaborar
        #
        #                     elif ingrediente.insumo.get_cantidad_existente_insumo() <= 0:
        #                         cantidad = 0
        #
        #                 if cantidad <= 0:
        #                     raise ValidationError('El Producto Compuesto (Comida) seleccionado no posee stock '
        #                                           'disponible en el %s. Verifique con el Encargado de este Deposito.'
        #                                           % deposito)
        #                 elif detalle_pedido.cantidad_producto_pedido > cantidad:
        #                     self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = False
        #                     raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto Compuesto (Comida)'
        #                                                                       'seleccionado supera el stock disponible en el "%s". '
        #                                                                       'Modifique la cantidad solicitada o cancele '
        #                                                                       'el pedido de este Producto.' % deposito})
        #
        #             # Si el ProductoCompuesto es una BEBIDA se debe verificar la disponibilidad de los Insumos en el Deposito del Sector desde donde se realiza el Pedido o VentaOcasional
        #             elif detalle_pedido.producto_pedido.categoria.categoria == 'BE':
        #                 # deposito = str(detalle_venta.venta.apertura_caja.sector.deposito.deposito)
        #                 # deposito = deposito.lower()
        #                 deposito = jornada.sector.deposito
        #                 det_prod_compuesto = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=detalle_pedido.producto_pedido.pk)
        #                 cantidad = 0
        #
        #                 # Verifica la Cantidad Existente de cada Insumo para el Deposito desde donde se esta registrando el Pedido.
        #                 for insumo in det_prod_compuesto:
        #                     productos = Producto.objects.filter(insumo_id=insumo.insumo.id, tipo_producto='IN')
        #                     cant_existente = 0
        #
        #                     for producto in productos:
        #                         try:
        #                             prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
        #                             cant_existente += prod_exist_deposito.cantidad_existente
        #                         except StockDepositoAjusteInventario.DoesNotExist:
        #                             pass
        #
        #                     if cant_existente > 0:
        #                         cant_posible_elaborar = cant_existente / (insumo.cantidad_insumo if insumo.cantidad_insumo else 1)
        #
        #                         if insumo == det_prod_compuesto.first():
        #                             cantidad = cant_posible_elaborar
        #
        #                         elif cant_posible_elaborar < cantidad:
        #                             cantidad = cant_posible_elaborar
        #
        #                     elif cant_existente <= 0:
        #                         cantidad = 0
        #
        #                 if cantidad <= 0:
        #                     raise ValidationError('El Producto Compuesto (Bebida) seleccionado no posee stock '
        #                                           'disponible en el %s. Verifique con el Encargado de este Deposito.' % deposito)
        #                 elif detalle_pedido.cantidad_producto_pedido > cantidad:
        #                     self.fields['cantidad_producto_pedido'].widget.attrs['readonly'] = False
        #                     raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto Compuesto (Bebida)'
        #                                                                       'seleccionado supera el stock disponible en el "%s". '
        #                                                                       'Modifique la cantidad solicitada o cancele '
        #                                                                       'el pedido de este Producto.' % deposito})
        # # ======================================================================================================================

# ======================================================================================================================
#         elif '_cancel' in self.request.POST:
#
#             import pdb
#             pdb.set_trace()
#
#             # Se anula esta validacion ya que los Productos ya son descontados del Stock al momento de guardar el Pedido.
#
#             if detalle_pedido.pk and detalle_pedido.procesado is True and detalle_pedido.pedido.estado_pedido.pedido_estado == 'VIG' \
#                     and detalle_pedido.pedido.jornada.estado_jornada in ('EXP', 'CER'):
#                 raise ValidationError('Este Producto ya fue procesado por lo tanto el Pedido no puede ser Cancelado. '
#                                       'Consulte con su Supervisor para definir el procedimiento a seguir.')
#             elif detalle_pedido.pk and detalle_pedido.procesado is True and detalle_pedido.pedido.estado_pedido.pedido_estado == 'VIG' \
#                     and detalle_pedido.pedido.jornada.estado_jornada == 'VIG':
#                 raise ValidationError({'producto_pedido': 'Este Producto ya fue procesado por lo tanto el Pedido no '
#                                                           'puede ser Cancelado. Consulte con su Supervisor para '
#                                                           'definir el procedimiento a seguir.'})
#
        return cleaned_data


class PedidoForm(forms.ModelForm):
    sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
                             label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
                             required=False)
    estado_jornada = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: goldenrod;'}),
                                     label=mark_safe('<strong style="font-size: 14px;">Estado Jornada</strong>'),
                                     required=False)
    id_cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 100px;'}), label='ID Cliente', required=False)
    cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Nombre Cliente', required=False)
    doc_ruc_cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Documento Reserva', required=False)
    # monto_entrega_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Monto Entrega Reserva', required=False, initial=0)
    monto_entrega_reserva = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                            label=mark_safe('<strong style="font-size: 14px;">Monto Entrega Reserva</strong>'),
                                            required=False, initial=0)
    mesas_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 900px;'}), label='Mesas Reservadas', required=False)
    # mesas_reserva = forms.ModelChoiceField(queryset=Mesa.objects.all(), label='Mesas Reserva', required=False)

    total_pedido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                   label=mark_safe('<strong style="font-size: 20px;">Total Pedido</strong>'),
                                   required=False, initial=0)

    class Meta:
        model = Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # result = super(PedidoForm, self).__init__(*args, **kwargs)
        super(PedidoForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        # self.fields['id_cliente_reserva'].widget.attrs['style'] = 'width: 500px;'

        pedido = self.instance

        usuario = Empleado.objects.get(usuario=self.request.user)

        if not pedido.pk:
            self.initial['mozo_pedido'] = usuario.id
            self.fields['mozo_pedido'].queryset = Empleado.objects.filter(usuario=usuario.usuario)
            # self.fields['mozo_pedido'].widget.attrs['readonly'] = True
            try:
                jornada = InicioJornada.objects.get(mozo=usuario, estado_jornada__in=['VIG', 'EXP'])

                # Verifica si la Jornada se encuentra EXP y en caso afirmativo asigna este estado al registro de la Jornada
                now = timezone.localtime(timezone.now())
                if jornada.estado_jornada == 'VIG' and timezone.localtime(jornada.fecha_hora_fin_jornada) < now:
                    jornada.estado_jornada = 'EXP'
                    jornada.save()

                self.initial['jornada'] = jornada.id
                self.fields['jornada'].queryset = InicioJornada.objects.filter(mozo=usuario, estado_jornada__in=['VIG', 'EXP'])
                self.initial['estado_jornada'] = jornada.get_estado_jornada_display()
                if jornada.estado_jornada == 'VIG':
                    self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'})
                elif jornada.estado_jornada == 'EXP':
                    self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: red;'})
                elif jornada.estado_jornada == 'CER':
                    self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: orange;'})

                if usuario.usuario.is_superuser is True:
                    self.initial['sector'] = Sector.objects.get(sector='BPR')
                elif usuario.cargo.cargo == 'BM':
                    self.initial['sector'] = jornada.sector
                    self.fields['mesa_pedido'].queryset = Mesa.objects.filter(numero_mesa=9999)
                else:
                    self.initial['sector'] = jornada.sector
                    self.fields['mesa_pedido'].queryset = Mesa.objects.filter(~Q(numero_mesa=9999))

            except ObjectDoesNotExist:
                self.initial['jornada'] = None
                self.fields['jornada'].queryset = InicioJornada.objects.none()
                # raise ValidationError('No existe una Jornada con estado Vigente para el Mozo/Barman %s. '
                #                       'Realice un Inicio de Jornada y vuelva a intentar registrar el '
                #                       'pedido.' % usuario.nombre_completo)
                self.initial['estado_jornada'] = None

        if pedido.pk:

            # Verifica si la Jornada se encuentra EXP y en caso afirmativo asigna este estado al registro de la Jornada
            jornada_elegida = pedido.jornada
            now = timezone.localtime(timezone.now())
            if jornada_elegida.estado_jornada == 'VIG' and timezone.localtime(jornada_elegida.fecha_hora_fin_jornada) < now:
                jornada_elegida.estado_jornada = 'EXP'
                jornada_elegida.save()

            self.initial['estado_jornada'] = pedido.jornada.get_estado_jornada_display()
            if pedido.jornada.estado_jornada == 'VIG':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'})
            elif pedido.jornada.estado_jornada == 'EXP':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: red;'})
            elif pedido.jornada.estado_jornada == 'CER':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: orange;'})

            if usuario.usuario.is_superuser is True:
                self.initial['sector'] = Sector.objects.get(sector='BPR')
            elif usuario.cargo.cargo == 'BM':
                self.initial['sector'] = pedido.jornada.sector
                self.fields['mesa_pedido'].queryset = Mesa.objects.filter(numero_mesa=9999)
            else:
                self.initial['sector'] = pedido.jornada.sector
                self.fields['mesa_pedido'].queryset = Mesa.objects.filter(~Q(numero_mesa=9999))

            if pedido.reserva is not None:
                self.initial['id_cliente_reserva'] = pedido.reserva.cliente.id
                self.initial['cliente_reserva'] = pedido.reserva.cliente.nombre_completo

                # Formatear correctamente los campos "doc_ruc_cliente_reserva" y "mesas_reserva" que manejan relaciones ManyToMany en la pantalla de Pedidos
                # self.initial['doc_ruc_cliente_reserva'] = "%s" % pedido.reserva.cliente.clientedocumento_set.all()
                # documentos = [("%s-%s" % (o, str(calcular_dv(o.numero_documento, 11)) if o.tipo_documento.documento == 'RUC' else 0)) ]

                # documentos = []
                # for o in pedido.reserva.cliente.clientedocumento_set.all():
                #     if o.tipo_documento.documento == 'RUC':
                #         documentos.append(('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11)))))
                #     else:
                #         documentos.append(('%s: %s' % (o.tipo_documento.documento, o.numero_documento)))
                #
                # self.initial['doc_ruc_cliente_reserva'] = ", ".join(documentos)
                self.initial['doc_ruc_cliente_reserva'] = pedido.reserva.cliente_documento_reserva
                self.initial['monto_entrega_reserva'] = pedido.reserva.pago
                # mesas_reserva = []
                # for m in pedido.reserva.mesas.all():
                #     mesas_reserva.append(str(m))

                self.initial['mesas_reserva'] = "| ".join([str(m) for m in pedido.reserva.mesas.all()])
                # self.fields['mesas_reserva'].choices = pedido.reserva.mesas.all().values_list('numero_mesa', 'nombre_mesa')
                # self.fields['mesas_reserva'].widget.attrs['disabled'] = True

        # return result

    def clean(self):
        cleaned_data = super(PedidoForm, self).clean()

        # import pdb
        # pdb.set_trace()

        pedido_actual = self.instance

        if "_continue" in self.request.POST or "_save" in self.request.POST:
            usuario = Empleado.objects.get(usuario=self.request.user)

            if pedido_actual.pk:

                # Verifica si la Jornada se encuentra EXP y en caso afirmativo asigna este estado al registro de la Jornada
                jornada_elegida = pedido_actual.jornada
                now = timezone.localtime(timezone.now())
                if jornada_elegida.estado_jornada == 'VIG' and timezone.localtime(jornada_elegida.fecha_hora_fin_jornada) < now:
                    jornada_elegida.estado_jornada = 'EXP'
                    jornada_elegida.save()
                # if pedido_actual.jornada.estado_jornada == 'EXP':
                    raise ValidationError('La Jornada con la que fue registrada el Pedido se encuentra '
                                          'expirada. Ya no puede realizar modificaciones sobre el '
                                          'Pedido, solo cancelarlo o cambiarlo de Jornada.')
                elif jornada_elegida.estado_jornada == 'EXP':
                    raise ValidationError('La Jornada con la que fue registrada el Pedido se encuentra '
                                          'expirada. Ya no puede realizar modificaciones sobre el '
                                          'Pedido, solo cancelarlo o cambiarlo de Jornada.')
                elif pedido_actual.jornada.estado_jornada == 'CER':
                    raise ValidationError('La Jornada con la que fue registrada el Pedido se encuentra '
                                          'cerrada. Ya no puede realizar modificaciones sobre el '
                                          'Pedido, solo cancelarlo o cambiarlo de Jornada.')
            elif not pedido_actual.pk:
                try:
                    jornada = InicioJornada.objects.get(mozo=usuario, estado_jornada__in=['VIG', 'EXP'])

                    # Verifica si la Jornada se encuentra EXP y en caso afirmativo asigna este estado al registro de la Jornada
                    now = timezone.localtime(timezone.now())
                    if jornada.estado_jornada == 'VIG' and timezone.localtime(jornada.fecha_hora_fin_jornada) < now:
                        jornada.estado_jornada = 'EXP'
                        jornada.save()
                        raise ValidationError({'mozo_pedido': 'El Mozo/Barman posee una Jornada expirada. Realice el '
                                                              'Cierre de la Jornada expirada e Inicie una nueva Jornada '
                                                              'para registrar pedidos.'})
                    elif jornada.estado_jornada == 'EXP':
                        raise ValidationError({'mozo_pedido': 'El Mozo/Barman posee una Jornada expirada. Realice el '
                                                              'Cierre de la Jornada expirada e Inicie una nueva Jornada '
                                                              'para registrar pedidos.'})
                except ObjectDoesNotExist:
                    raise ValidationError({'mozo_pedido': 'El Mozo/Barman NO posee una Jornada vigente. Realice un Inicio '
                                                          'de Jornada para registrar pedidos.'})

            now = timezone.localtime(timezone.now())
            hora_actual = now.time()
            hora_inicio_reservas = datetime.time(hour=18, minute=0)
            hora_fin_reservas = datetime.time(hour=21, minute=0)

            if not pedido_actual.pk:
                # Si la hora actual no esta comprendida entre "hora_inicio_reservas" y "hora_fin_reservas" no se debe permitir utilizar la Reserva
                id_reserva = self.data.get('reserva', None)
                # try:
                if id_reserva is not None and id_reserva != '':
                    reserva_elegida = Reserva.objects.get(pk=id_reserva)
                    if reserva_elegida is not None and hora_actual > hora_fin_reservas \
                            or reserva_elegida is not None and hora_actual < hora_inicio_reservas:
                    # if reserva_elegida is not None and timezone.localtime(timezone.now()) < reserva_elegida.fecha_hora_reserva:
                        raise ValidationError({'reserva': 'Las Reservas de Mesas pueden ser utilizadas unicamente '
                                                          'entre las %s y %s. Aguarde el horario indicado para '
                                                          'utilizar la Reserva.' % (hora_inicio_reservas, hora_fin_reservas)})
                # except ObjectDoesNotExist or ValueError:
                #     pass

            # ==========================================================================================================
            # Validar que las Mesas seleccionadas tengan estado "DI"
            # ==========================================================================================================
            if pedido_actual.pk:
                mesas_guardadas = pedido_actual.mesa_pedido.all()
            else:
                mesas_guardadas = None

            # mesa = self.data.get('mesa_pedido', None)
            # if mesa is not None:
            #     mesa_elegida = Mesa.objects.get(pk=mesa)
            # else:
            #     mesa_elegida = None

            try:
                for mesa_elegida in self.cleaned_data['mesa_pedido']:
                    if mesa_elegida is not None and mesas_guardadas is None or \
                                                    mesa_elegida is not None and mesas_guardadas is not None and mesa_elegida not in mesas_guardadas:
                        if mesa_elegida.estado.mesa_estado == 'IN':
                            raise ValidationError({'mesa_pedido': '%s se encuentra inactiva. Seleccione otra Mesa.' % mesa_elegida})
                        elif mesa_elegida.estado.mesa_estado == 'OC':
                            raise ValidationError({'mesa_pedido': '%s ya se encuentra ocupada. Seleccione otra Mesa.' % mesa_elegida})

                # ==========================================================================================================
                # Validar que las Mesas seleccionadas no esten Reservadas
                # Tener en cuenta que las Reservas se pueden realizar y usufructuar entre las 18:00 y 21:00 hs
                # ==========================================================================================================
                now = timezone.localtime(timezone.now())
                hora_actual = now.time()
                hora_inicio_reservas = datetime.time(hour=18, minute=0)
                hora_fin_reservas = datetime.time(hour=21, minute=0)
                # ===> inicio_reservas, fin_reservas, reservas2, reservas3 calculados para probar el limit_choices_to del campo "reserva" <===
                # inicio_reservas = timezone.make_aware(datetime.datetime.combine(now.date(), hora_inicio_reservas), timezone.get_default_timezone())
                # fin_reservas = timezone.make_aware(datetime.datetime.combine(now.date(), hora_fin_reservas), timezone.get_default_timezone())
                # hora_reserva = self.fecha_hora_reserva.time()

                # Si el Pedido no tiene una Reserva y la hora_actual esta comprendida entre las 18 y 21 hs entonces se
                # debe verificar si existe alguna Reserva de Mesas, de lo contrario solo debe realizar la validacion
                # ya realizada anteriormente.
                posee_reserva = self.data.get('reserva', None)
                if posee_reserva is None and hora_fin_reservas >= hora_actual and hora_actual >= hora_inicio_reservas \
                        or posee_reserva == '' and hora_fin_reservas >= hora_actual and hora_actual >= hora_inicio_reservas:
                        # or pedido_actual.reserva is None and hora_fin_reservas >= hora_actual and hora_actual >= hora_inicio_reservas:

                    reservas = Reserva.objects.filter(fecha_hora_reserva__year=now.year,
                                                      fecha_hora_reserva__month=now.month,
                                                      fecha_hora_reserva__day=now.day,
                                                      estado__reserva_estado='VIG')
                    # reservas2 = Reserva.objects.filter(fecha_hora_reserva__gte=inicio_reservas, fecha_hora_reserva__lte=fin_reservas, estado__reserva_estado='VIG')
                    # reservas3 = Reserva.objects.filter(fecha_hora_reserva__gte=timezone.make_aware(datetime.datetime.combine(timezone_today(), datetime.time(hour=18, minute=0)), timezone.get_default_timezone()), fecha_hora_reserva__lte=timezone.make_aware(datetime.datetime.combine(timezone_today(), datetime.time(hour=21, minute=0)), timezone.get_default_timezone()), estado__reserva_estado='VIG')

                    for reserva in reservas:
                        mesas_reservadas = reserva.mesas.all()

                        for mesa_elegida in self.cleaned_data['mesa_pedido']:
                            # Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
                            if mesa_elegida is not None and mesas_reservadas is not None and mesa_elegida in mesas_reservadas:
                                raise ValidationError({'mesa_pedido': '%s ya se encuentra reservada para la fecha indicada. '
                                                                      'Seleccione otra Mesa.' % mesa_elegida})
                # # Si la hora actual no es mayor o igual a la hora de la Reserva no se debe permitir utilizar la Reserva
                # elif posee_reserva is not None and now < posee_reserva.fecha_hora_reserva:
                #     raise ValidationError({'reserva': 'La hora actual es menor a la fecha/hora de la Reserva. Si desea '
                #                                       'adelantar la utilizacion de la Reserva modifique la hora en la '
                #                                       'misma.'})

            except KeyError:
                pass

        # if '_cancel' in self.request.POST:
        #     if detalle_pedido.pk and detalle_pedido.procesado is True:
        #         raise ValidationError({'producto_pedido': 'Este Producto ya fue procesado por lo tanto el Pedido no '
        #                                                   'puede ser Cancelado. Consulte con su Supervisor para '
        #                                                   'definir el procedimiento a seguir.'})

        return cleaned_data


class VentaOcasionalDetalleForm(forms.ModelForm):
    
    class Meta:
        model = VentaDetalle
        fields = '__all__'

    def clean(self):
        cleaned_data = super(VentaOcasionalDetalleForm, self).clean()

        import pdb
        pdb.set_trace()

        detalle_venta = self.instance
        apertura_caja = AperturaCaja.objects.none
        if detalle_venta.pk:
            apertura_caja = AperturaCaja.objects.get(pk=detalle_venta.venta.apertura_caja.id)
        elif not detalle_venta.pk:
            if self.data.get('apertura_caja') != '':
                apertura_caja = AperturaCaja.objects.get(pk=self.data.get('apertura_caja'))
            else:
                pass

        # No se requiere verificar si la Venta es Ocasional ya que este form afecta solo a VentaOcasionalDetalleInline
        # if detalle_venta.venta.venta_ocasional is True:

        # if "_addanother" in self.request.POST or "_save" in self.request.POST:
            # Validar la Cantidad Existente del Producto seleccionado
        if not detalle_venta.pk:
            if 'producto_venta' not in self.cleaned_data:
                raise ValidationError({'producto_venta': 'Debe seleccionar un Producto para completar la Venta.'})
            elif self.cleaned_data['producto_venta'].get_cantidad_existente_producto() <= 0:
                if self.cleaned_data['producto_venta'].compuesto is False:
                    raise ValidationError({'producto_venta': 'El Producto seleccionado no posee stock disponible. '
                                                             'Seleccione otro Producto.'})
                elif self.cleaned_data['producto_venta'].compuesto is True:
                    raise ValidationError({'producto_venta': 'El Producto Compuesto seleccionado no posee stock '
                                                             'disponible en todos o algunos de sus insumos. '
                                                             'Seleccione otro Producto.'})
            # Verificar disponible en Deposito del Sector
            elif self.cleaned_data['producto_venta'].compuesto is False:
                try:
                    producto_por_deposito = StockDepositoAjusteInventario.objects.get(id=self.cleaned_data['producto_venta'].id, deposito_id=apertura_caja.sector.deposito.id)
                    if producto_por_deposito.cantidad_existente <= 0:
                        raise ValidationError({'producto_venta': 'El Producto seleccionado no posee stock disponible '
                                                                 'en el "%s" de su sector "%s". Verifique con el Encargado de '
                                                                 'Deposito de su sector.' % (apertura_caja.sector.deposito, apertura_caja.sector)})
                    elif self.cleaned_data['cantidad_producto_venta'] > producto_por_deposito.cantidad_existente:
                        # self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False
                        raise ValidationError({'cantidad_producto_venta': 'La cantidad solicitada del Producto '
                                                                          'seleccionado supera el stock disponible en el "%s" de su sector "%s". '
                                                                          'Modifique la cantidad solicitada o cancele '
                                                                          'el pedido de este Producto.' % (apertura_caja.sector.deposito, apertura_caja.sector)})
                except StockDepositoAjusteInventario.DoesNotExist:
                    raise ValidationError({'producto_venta': 'El Producto seleccionado no posee stock disponible en '
                                                             'el "%s" de su sector "%s". Verifique con el Encargado de Deposito '
                                                             'de su sector.' % (apertura_caja.sector.deposito, apertura_caja.sector)})

            elif self.cleaned_data['producto_venta'].compuesto is True:
                # Si el ProductoCompuesto es una COMIDA se debe verificar la disponibilidad de los Insumos en el Deposito de la Cocina
                if self.cleaned_data['producto_venta'].categoria.categoria == 'CO':
                    deposito = Deposito.objects.get(deposito='DCO')
                    ingredientes = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=self.cleaned_data['producto_venta'].pk)
                    cantidad = 0
                    for ingrediente in ingredientes:
                        if ingrediente.insumo.get_cantidad_existente_insumo_dco() > 0:
                            cant_posible_elaborar = ingrediente.insumo.get_cantidad_existente_insumo_dco() / (ingrediente.cantidad_insumo if ingrediente.cantidad_insumo else 1)
        
                            if ingrediente == ingredientes.first():
                                cantidad = cant_posible_elaborar
        
                            elif cant_posible_elaborar < cantidad:
                                cantidad = cant_posible_elaborar
        
                        elif ingrediente.insumo.get_cantidad_existente_insumo_dco() <= 0:
                            cantidad = 0
                    
                    if cantidad <= 0:
                        raise ValidationError({'producto_venta': 'El Producto Compuesto (Comida) seleccionado no posee stock '
                                                                 'disponible en el "%s". Verifique con el Encargado de '
                                                                 'este Deposito.' % deposito})
                    elif self.cleaned_data['cantidad_producto_venta'] > cantidad:
                        # self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False
                        raise ValidationError({'cantidad_producto_venta': 'La cantidad solicitada del Producto Compuesto (Comida)'
                                                                          'seleccionado supera el stock disponible en el "%s". '
                                                                          'Modifique la cantidad solicitada o cancele '
                                                                          'el pedido de este Producto.' % deposito})
                # Si el ProductoCompuesto es una BEBIDA se debe verificar la disponibilidad de los Insumos en el Deposito del Sector desde donde se realiza el Pedido o VentaOcasional
                elif self.cleaned_data['producto_venta'].categoria.categoria == 'BE':
                    # deposito = str(detalle_venta.venta.apertura_caja.sector.deposito.deposito)
                    # deposito = deposito.lower()
                    deposito = apertura_caja.sector.deposito
                    det_prod_compuesto = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=self.cleaned_data['producto_venta'].pk)
                    cantidad = 0

                    # Verifica la Cantidad Existente de cada Insumo para el Deposito desde donde se esta registrando el Pedido.
                    for insumo in det_prod_compuesto:
                        productos = Producto.objects.filter(insumo_id=insumo.insumo.id, tipo_producto='IN')
                        cant_existente = 0

                        for producto in productos:
                            try:
                                prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                cant_existente += prod_exist_deposito.cantidad_existente
                            except StockDepositoAjusteInventario.DoesNotExist:
                                pass
                        
                        if cant_existente > 0:
                            cant_posible_elaborar = cant_existente / (insumo.cantidad_insumo if insumo.cantidad_insumo else 1)

                            if insumo == det_prod_compuesto.first():
                                cantidad = cant_posible_elaborar

                            elif cant_posible_elaborar < cantidad:
                                cantidad = cant_posible_elaborar

                        elif cant_existente <= 0:
                            cantidad = 0
                    
                    if cantidad <= 0:
                        raise ValidationError({'producto_venta': 'El Producto Compuesto (Bebida) seleccionado no posee stock '
                                                                 'disponible en el "%s". Verifique con el Encargado de '
                                                                 'este Deposito.' % deposito})        
                    elif self.cleaned_data['cantidad_producto_venta'] > cantidad:
                        # self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False
                        raise ValidationError({'cantidad_producto_venta': 'La cantidad solicitada del Producto Compuesto (Bebida) '
                                                                          'seleccionado supera el stock disponible en el "%s". '
                                                                          'Modifique la cantidad solicitada o cancele '
                                                                          'el pedido de este Producto.' % deposito})

            # # No aplica porque en la pantalla de Ventas Ocasionales no se guardan borradores del Pedido de los Productos, directamente se confirma la Venta.
            # elif detalle_venta.pk:
            #     if detalle_venta.producto_venta.get_cantidad_existente_producto() <= 0:
            #         if detalle_venta.producto_venta.compuesto is False:
            #             raise ValidationError('El Producto seleccionado no posee stock disponible. Seleccione otro '
            #                                   'Producto.')
            #         elif detalle_venta.producto_venta.compuesto is True:
            #             raise ValidationError('El Producto Compuesto seleccionado no posee stock disponible en todos o '
            #                                   'algunos de sus insumos. Seleccione otro Producto.')
            #     elif detalle_venta.cantidad_producto_venta > detalle_venta.producto_venta.get_cantidad_existente_producto():
            #         self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False
            #         raise ValidationError({'cantidad_producto_venta': 'La cantidad solicitada del Producto '
            #                                                           'seleccionado supera el stock disponible. '
            #                                                           'Modifique la cantidad solicitada o cancele el '
            #                                                           'pedido de este Producto.'})

        return cleaned_data
        

class VentaForm(forms.ModelForm):
    # timbrado = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Timbrado', required=False)
    fecha_limite_vigencia_timbrado = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha Vigencia Timbrado', required=False)
    caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Caja', required=False)
    cajero = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Cajero', required=False)
    sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
                             label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
                             required=False)
    estado_apertura_caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: goldenrod;'}),
                                           label=mark_safe('<strong style="font-size: 14px;">Estado Apert. Caja</strong>'),
                                           required=False)
    horario = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario', required=False)
    fecha_hora_apertura_caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha/hora Apertura', required=False)

    total_pedido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                   label=mark_safe('<strong style="font-size: 14px;">Total Pedido</strong>'),
                                   required=False, initial=0)

    # posee_reserva = forms.BooleanField(label='Posee reserva?', required=False)
    posee_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 500px; font-size: 14px; height: 20px; font-weight: bold; color: goldenrod;'}), label='Reserva', required=False)
    entrega_reserva = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                      label=mark_safe('<strong style="font-size: 14px;">Monto Entrega Reserva</strong>'),
                                      required=False, initial=0)
    doc_ruc_cliente_reserva = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Documento guardado', required=False)
    cliente_documento_factura = forms.CharField(widget=forms.Select(attrs={'class':'hidden'}), label='Documentos disponibles', required=False)
    # cliente_documento_factura = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'hidden'}), queryset=ClienteDocumento.objects.all, label='Documento', required=False)
    direccion_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Direccion', required=False)
    pais_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Pais', required=False)
    ciudad_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Ciudad', required=False)
    telefonos_cliente = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 500px;'}), label='Telefonos', required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 300px;'}), label='Email', required=False)

    total_venta = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                  label=mark_safe('<strong style="font-size: 20px;">Total Venta</strong>'),
                                  required=False, initial=0)
    # efectivo_recibido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
    #                                     label=mark_safe('<strong style="font-size: 20px;">Efectivo Recibido</strong>'),
    #                                     required=False, initial=0)
    vuelto = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                             label=mark_safe('<strong style="font-size: 20px;">Vuelto</strong>'),
                             required=False, initial=0)
    
    class Meta:
        model = Venta
        fields = '__all__'
        # widgets = {
        #     # 'cliente_documento_factura': forms.ChoiceField(widget=forms.Select(attrs={'class':'hidden'}), label='Documento', required=False),
        #     # 'cliente_documento_factura': autocomplete.ModelSelect2(url='ventas:clientedocumento-autocomplete', forward=['cliente_factura']),
        #     # 'apertura_caja': forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 400px;'}), label='Apertura de Caja', required=False)
        # }

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)

    # def is_valid(self):
    #     super(VentaForm, self).is_valid()

        # import pdb
        # pdb.set_trace()

        venta = self.instance

        if not venta.pk:
            # empresa = Empresa.objects.get(pk=self.data.get('empresa', ''))
            empresa = venta.empresa
            # if empresa.timbrado.estado_timbrado == 'IN':
            #     # raise forms.ValidationError({'timbrado': 'El Timbrado esta inactivo. Verifique los datos de la Empresa.'})
            #     raise forms.ValidationError('El Timbrado esta inactivo. Verifique los datos de la Empresa.')
            # elif empresa.timbrado.fecha_limite_vigencia_timbrado < timezone.now().date():
            #     # raise ValidationError({'timbrado': 'El Timbrado esta vencido. Verifique los datos de la Empresa.'})
            #     raise ('El Timbrado esta vencido. Verifique los datos de la Empresa.')
            # else:
            self.initial['timbrado'] = empresa.timbrado.id
            self.initial['fecha_limite_vigencia_timbrado'] = datetime.datetime.strftime(empresa.timbrado.fecha_limite_vigencia_timbrado, '%d/%m/%Y')

            usuario = Empleado.objects.get(usuario=self.request.user)

            try:
                apertura = AperturaCaja.objects.get(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP'])
                # if apertura is None:
                #     # raise ValidationError({'apertura_caja': 'El Cajero NO posee una Apertura de Caja vigente. Realice una '
                #     #                                         'Apertura de Caja para poder registrar ventas.'})
                #     raise ('El Cajero NO posee una Apertura de Caja vigente. Realice una Apertura de Caja para poder '
                #            'registrar ventas.')
                # else:

                now = timezone.localtime(timezone.now())
                if timezone.localtime(apertura.fecha_hora_fin_apertura_caja) < now:
                    apertura.estado_apertura_caja = 'EXP'
                    apertura.save()

                self.initial['apertura_caja'] = apertura.id
                self.fields['apertura_caja'].queryset = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP'])
                self.initial['cajero'] = apertura.cajero
                self.initial['caja'] = apertura.caja
                self.initial['horario'] = apertura.horario
                self.initial['fecha_hora_apertura_caja'] = datetime.datetime.strftime(timezone.localtime(apertura.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')
                # self.fields['apertura_caja'].widget.attrs['readonly'] = True
                # self.fields['apertura_caja'].widget.attrs['disabled'] = True

                self.initial['estado_apertura_caja'] = apertura.get_estado_apertura_caja_display()
                if apertura.estado_apertura_caja == 'VIG':
                    self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'})
                elif apertura.estado_apertura_caja == 'EXP':
                    self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: red;'})
                elif apertura.estado_apertura_caja == 'CER':
                    self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: orange;'})

                if usuario.usuario.is_superuser is True:
                    self.initial['sector'] = Sector.objects.get(sector='BPR')
                elif usuario.cargo.cargo == 'CA':
                    self.initial['sector'] = apertura.sector
                    # self.fields['mesa_pedido'].queryset = Mesa.objects.filter(numero_mesa=9999)
                else:
                    self.initial['sector'] = apertura.sector
                    # self.fields['mesa_pedido'].queryset = Mesa.objects.filter(~Q(numero_mesa=9999))

            except ObjectDoesNotExist:
                self.initial['apertura_caja'] = None
                self.fields['apertura_caja'].queryset = AperturaCaja.objects.none()
                # raise ValidationError('No existe una Jornada con estado Vigente para el Mozo/Barman %s. '
                #                       'Realice un Inicio de Jornada y vuelva a intentar registrar el '
                #                       'pedido.' % usuario.nombre_completo)
                self.initial['estado_apertura_caja'] = None

        elif venta.pk:
            if venta.estado_venta.venta_estado == 'PEN':
                self.initial['apertura_caja'] = venta.apertura_caja.id
                self.fields['apertura_caja'].queryset = AperturaCaja.objects.filter(pk=venta.apertura_caja.id)
                # self.fields['apertura_caja'].widget.attrs['readonly'] = True
                # self.fields['apertura_caja'].widget.attrs['style'] = 'width: 300px;'
                # self.fields['timbrado'].widget.attrs['readonly'] = True

            # self.initial['timbrado'] = venta.empresa.timbrado.timbrado
            self.initial['fecha_limite_vigencia_timbrado'] = datetime.datetime.strftime(venta.timbrado.fecha_limite_vigencia_timbrado, '%d/%m/%Y')
            self.initial['numero_factura_venta'] = venta.numero_factura_venta.numero_factura
            self.initial['fecha_hora_apertura_caja'] = datetime.datetime.strftime(timezone.localtime(venta.apertura_caja.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')
            self.initial['caja'] = venta.apertura_caja.caja
            self.initial['cajero'] = venta.apertura_caja.cajero
            self.initial['horario'] = venta.apertura_caja.horario
            self.initial['sector'] = venta.apertura_caja.sector

            self.initial['estado_apertura_caja'] = venta.apertura_caja.get_estado_apertura_caja_display()
            if venta.apertura_caja.estado_apertura_caja == 'VIG':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'})
            elif venta.apertura_caja.estado_apertura_caja == 'EXP':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: red;'})
            elif venta.apertura_caja.estado_apertura_caja == 'CER':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 14px; height: 20px; font-weight: bold; color: orange;'})

            if venta.numero_pedido is not None:
                self.initial['total_pedido'] = venta.numero_pedido.total_pedido

                if venta.numero_pedido.reserva is None:
                    self.initial['posee_reserva'] = 'No posee Reserva'
                elif venta.numero_pedido.reserva is not None:
                    self.initial['posee_reserva'] = venta.numero_pedido.reserva
                    self.initial['entrega_reserva'] = venta.numero_pedido.reserva.pago

                # import pdb
                # pdb.set_trace()

            if venta.cliente_factura is not None:

                # import pdb
                # pdb.set_trace()

                # options = []
                # for o in venta.cliente_factura.clientedocumento_set.all():  # filter(cliente_id=venta.cliente_factura):
                #     if o.tipo_documento.documento == 'RUC':
                #         options += [("%s-%s" % (o.numero_documento, str(calcular_dv(o.numero_documento, 11)))), "%s-%s" % (o, str(calcular_dv(o.numero_documento, 11)))]
                #     else:
                #         options += [("%s" % o.numero_documento, "%s" % o)]

                # import pdb
                # pdb.set_trace()

                # ===> Carga el ChoiceField con todos los numeros de documento del Cliente. <===
                documentos = []
                for o in ClienteDocumento.objects.all():  # venta.cliente_factura.clientedocumento_set.all():
                    if o.tipo_documento.documento == 'RUC':
                        documentos.append((('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11)))), ('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11))))),)
                    else:
                        documentos.append((('%s: %s' % (o.tipo_documento.documento, o.numero_documento)), ('%s: %s' % (o.tipo_documento.documento, o.numero_documento))),)
                # documentos[9999999] = 'Sin datos'
                documentos.append(('9999999', '9999999: Sin datos'),)

                # import pdb
                # pdb.set_trace()

                # documento_inicial = []
                # for o in venta.cliente_factura.clientedocumento:
                #     if o.tipo_documento.documento == 'RUC':
                #         documento_inicial.append((('%s-%s' % (o.numero_documento, str(calcular_dv(o.numero_documento, 11)))), ('%s: %s-%s' % (o.tipo_documento.documento, o.numero_documento, str(calcular_dv(o.numero_documento, 11))))),)
                #     else:
                #         documento_inicial.append((('%s' % o.numero_documento), ('%s: %s' % (o.tipo_documento.documento, o.numero_documento))),)

                # self.fields['cliente_documento_factura'] = forms.ChoiceField(choices=options, required=False, label='Documento Factura')
                # self.fields['cliente_documento_factura'] = forms.ChoiceField(choices=[(o.id, "%s-%s" % (o, str(calcular_dv(o.numero_documento, 11)) if o.tipo_documento.documento == 'RUC' else 0)) for o in venta.cliente_factura.clientedocumento_set.filter(cliente_id=venta.cliente_factura)])
                # self.fields['cliente_documento_factura'] = forms.ChoiceField(choices=[(o.id, str(o)) for o in ClienteDocumento.objects.filter(cliente_id=venta.cliente_factura)])
                # self.fields['cliente_documento_factura'] = forms.ChoiceField(ClienteDocumento.objects.filter(cliente_id=venta.cliente_factura).values_list('tipo_documento', 'numero_documento'))
                # self.fields['cliente_documento_factura'].choices = venta.cliente_factura.documentos.filter(cliente=venta.cliente_factura)
                self.fields['cliente_documento_factura'] = forms.ChoiceField(choices=documentos, required=False, label='Documentos disponibles', initial=venta.cliente_documento_factura)
                # self.initial['cliente_documento_factura'] = venta.cliente_documento_factura
                # self.initial['cliente_documento_factura'] = documento_inicial
                self.initial['doc_ruc_cliente_reserva'] = venta.cliente_documento_factura
                self.initial['direccion_cliente'] = venta.cliente_factura.direccion
                self.initial['pais_cliente'] = venta.cliente_factura.pais
                self.initial['ciudad_cliente'] = venta.cliente_factura.ciudad
                self.initial['telefonos_cliente'] = " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=venta.cliente_factura.pk)])
                self.initial['email'] = venta.cliente_factura.email

    def clean(self):
        cleaned_data = super(VentaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        venta = self.instance
        # print self.request.POST.get('cliente_documento_factura', '')

        if "_continue" in self.request.POST or "_save" in self.request.POST or "_addanother" in self.request.POST:
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
            apertura = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP'])
            if not apertura.exists():
                raise ValidationError({'apertura_caja': 'El Cajero NO posee una Apertura de Caja vigente. Realice una '
                                                        'Apertura de Caja para poder registrar ventas.'})
            elif apertura[0].estado_apertura_caja == 'EXP':
                raise ValidationError({'apertura_caja': 'El Cajero posee una Apertura de Caja expirada. Realice el '
                                                        'Cierre de Caja y posteriormente una nueva Apertura de Caja '
                                                        'para poder registrar ventas.'})
            elif apertura[0].en_proceso_cierre is True:
                raise ValidationError({'apertura_caja': 'El Cajero posee una Apertura de Caja vigente pero en Proceso de '
                                                        'Cierre. Complete el Cierre de Caja y realice una nueva Apertura '
                                                        'de Caja para poder registrar ventas.'})

            # Validaciones sobre el Pedido
            nro_pedido = self.data.get('numero_pedido')
            if venta.venta_ocasional is False and nro_pedido is not None:
                try:
                    pedido_elegido = Pedido.objects.get(pk=nro_pedido)
                    ventas_procesadas = Venta.objects.filter(numero_pedido_id=pedido_elegido.pk, estado_venta__venta_estado__in=['PRO', 'PEN'])
                    if ventas_procesadas.exists() and ventas_procesadas[0].id != venta.id:
                        raise ValidationError({'numero_pedido': 'El Pedido seleccionado ya se encuentra relacionado a '
                                                                'otra Venta. Seleccione otro Pedido.'})
                    elif pedido_elegido.reserva is not None and pedido_elegido.reserva.pago > pedido_elegido.total_pedido:
                        # Asignar el estado VIG al pedido_anterior => No es necesario, la Venta no termina de guardarse
                        # al seleccionar un Pedido en donde el Monto de Entrega de la Reserva es mayor que el Total del
                        # Pedido
                        raise ValidationError({'total_venta': 'El Monto Entrega de la Reserva no puede ser mayor que el Total del '
                                                              'Pedido. Cancele la Venta y verifique el Pedido.'})
                except ValueError:
                    if venta.venta_ocasional is False:
                        raise ValidationError({'numero_pedido': 'Debe seleccionar un Numero de Pedido para completar la Venta.'})
                    else:
                        pass

            # Validaciones sobre la Forma de Pago

            # import pdb
            # pdb.set_trace()

            if self.cleaned_data['forma_pago'] is None and "_continue" not in self.request.POST\
                    or self.cleaned_data['forma_pago'] == '' and "_continue" not in self.request.POST:
            # if venta.venta_ocasional is True and self.cleaned_data['forma_pago'] is None and "_continue" not in self.request.POST\
            #         or venta.venta_ocasional is True and self.cleaned_data['forma_pago'] == '' and "_continue" not in self.request.POST:
                raise ValidationError({'forma_pago': 'Debe seleccionar una Forma de Pago para completar la Venta.'})

            elif self.cleaned_data['forma_pago'] in ('EF', 'OM') and self.cleaned_data['efectivo_recibido'] == 0 and "_continue" not in self.request.POST\
                    or self.cleaned_data['forma_pago'] in ('EF', 'OM') and self.cleaned_data['efectivo_recibido'] is None and "_continue" not in self.request.POST:
                raise ValidationError({'efectivo_recibido': 'Debe ingresar el monto de Efectivo Recibido.'})

            elif self.cleaned_data['forma_pago'] in ('EF', 'OM') and int(self.cleaned_data['total_venta']) > int(self.cleaned_data['efectivo_recibido']) and "_continue" not in self.request.POST\
                    or self.cleaned_data['forma_pago'] in ('EF', 'OM') and self.cleaned_data['efectivo_recibido'] is not None and int(self.cleaned_data['total_venta']) > int(self.cleaned_data['efectivo_recibido']) and "_continue" not in self.request.POST:
                raise ValidationError({'efectivo_recibido': 'El monto del pago en Efectivo o en Otros Medios debe ser igual o mayor al monto del Total de la Venta.'})

            elif self.cleaned_data['forma_pago'] in ('TC', 'TD') and self.cleaned_data['voucher'] == 0 and "_continue" not in self.request.POST\
                    or self.cleaned_data['forma_pago'] in ('TC', 'TD') and self.cleaned_data['voucher'] is None and "_continue" not in self.request.POST\
                    or self.cleaned_data['forma_pago'] in ('TC', 'TD') and self.cleaned_data['voucher'] == '' and "_continue" not in self.request.POST:
                raise ValidationError({'voucher': 'Debe ingresar el numero de Voucher.'})

            # import pdb
            # pdb.set_trace()

            # Validaciones sobre el Cliente
            id_cliente = self.data.get('cliente_factura', None)
            if "_continue" not in self.request.POST and id_cliente is not None and id_cliente != '':
                doc_cliente = self.data.get('cliente_documento_factura', None)
                if "_continue" not in self.request.POST and doc_cliente is None\
                        or "_continue" not in self.request.POST and doc_cliente == '':
                    raise ValidationError({'cliente_documento_factura': 'Debe seleccionar un documento para el Cliente.'})

        # elif '_cancel' in self.request.POST:
        #     nro_pedido = self.data.get('numero_pedido')
        #     try:
        #         pedido = Pedido.objects.get(pk=nro_pedido)
        #     except ValueError:
        #         if venta.venta_ocasional is False:
        #             raise ValidationError({'numero_pedido': 'Debe seleccionar un Numero de Pedido para completar la Venta.'})
        #         else:
        #             pass
        #
        #     if venta.venta_ocasional is False and not venta.numero_pedido:
        #         raise ValidationError({'numero_pedido': 'Debe seleccionar un Numero de Pedido para completar la Venta.'})
        #     else:
        #         pass

        return cleaned_data


class AperturaCajaForm(forms.ModelForm):

    # cajero2 = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Cajero')
    # horario2 = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario')
    nombre_cajero = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Nombre Cajero', required=False)
    # sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
    #                          label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
    #                          required=False)
    # jornada = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Jornada', required=False,
    #                           help_text='Se genera automaticamente al Confirmar la Apertura de Caja.')
    duracion_apertura = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 60px;'}), label='Duracion Apert. Caja', required=False)
    # fecha_hora_fin_apertura_caja = forms.CharField(widget=forms.DateTimeField(format='%d/%m/%Y %H:%M:%S'), label='Fecha/hora Fin Apert. Caja', required=False)
    # fecha_hora_fin_apertura_caja = forms.CharField(widget=forms.DateTimeInput(), label='Fecha/hora Fin Apert. Caja', required=False)

    class Meta:
        model = AperturaCaja
        fields = '__all__'
        # widgets = {
        #     # 'cajero': forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Cajero', required=False),
        #     # 'fecha_hora_fin_apertura_caja': forms.DateTimeField(attrs={'class':'myDateClass'}),
        # }

    def __init__(self, *args, **kwargs):
        super(AperturaCajaForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        apertura = self.instance

        if apertura.pk:
            self.initial['nombre_cajero'] = apertura.cajero.nombre_completo

    def clean(self):
        cleaned_data = super(AperturaCajaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        # usuario = self.data.get('cajero', '')
        # print usuario

        apertura_caja = self.instance
        # apertura_caja.jornada = InicioJornada.objects.get(pk=1)
        # self.request.jornada = InicioJornada.objects.get(pk=1)

        if apertura_caja:
            usuario = Empleado.objects.get(usuario=self.request.user)
            if usuario.usuario.is_superuser is True:
                pass
            elif usuario.cargo.cargo != 'CA':
                raise ValidationError({'cajero': 'El Usuario no posee el cargo de Cajero. Modifique el cargo del '
                                                 'Usuario y vuelva a intentarlo.'})

            aperturas = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP'])
            if aperturas.exists():
                raise ValidationError({'cajero': 'El Cajero ya posee una Apertura de Caja vigente/expirada. Solo puede '
                                                 'tener una Caja abierta.'})

            jornadas = InicioJornada.objects.filter(mozo=usuario, estado_jornada__in=['VIG', 'EXP'])
            if jornadas.exists():
                raise ValidationError({'cajero': 'El Cajero ya posee un Inicio de Jornada vigente/expirado. Solo '
                                                 'puede tener un Inicio de Jornada vigente/expirado.'})

            id_caja = self.data.get('caja')
            try:
                caja = Caja.objects.get(pk=id_caja)
                if caja.estado_caja == 'ABI':
                    raise ValidationError({'caja': 'La Caja seleccionada se encuentra con estado ABIERTO.'})
            except ValueError:
                pass

        #     return apertura_caja.
        # else:
        #     return self.cleaned_data['cajero', 'horario']

        return cleaned_data


# class CierreCajaRawIdWidget(widgets.ForeignKeyRawIdWidget):
#     def url_parameters(self):
#         res = super(CierreCajaRawIdWidget, self).url_parameters()
#         usuario = self.attrs.get('object', None)
#         if usuario.usuario.is_superuser is True:
#             cierres = CierreCaja.objects.all().values('apertura_caja')
#             res['id'] = AperturaCaja.objects.filter(estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
#         else:
#             cierres = CierreCaja.objects.all().values('apertura_caja')
#             res['id'] = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
#
#         return res


class CierreCajaForm(forms.ModelForm):
    cajero = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Cajero', required=False)
    caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Caja', required=False)
    sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
                             label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
                             required=False)
    horario = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario', required=False)
    jornada = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Jornada', required=False)
    fecha_hora_apertura_caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha/hora Apertura', required=False)
    monto_apertura = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_apertura),
                                     label=mark_safe('<strong style="font-size: 14px;">Monto Apertura</strong>'),
                                     required=False, initial=0)
    estado_apertura_caja = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 15px; height: 30px; font-weight: bold; color: goldenrod;'}),
                                           label=mark_safe('<strong style="font-size: 14px;">Estado Apertura Caja</strong>'),
                                           required=False)

    cantidad_total_operaciones_pendientes = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Ventas Pendientes', required=False, initial=0)
    cantidad_total_operaciones_canceladas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Ventas Canceladas', required=False, initial=0)

# ==> Efectivo <==
    cantidad_operaciones_efectivo_procesadas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Efectivo Procesadas', required=False, initial=0)
    cantidad_operaciones_efectivo_pendientes = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Efectivo Pendientes', required=False, initial=0)
    cantidad_operaciones_efectivo_canceladas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Efectivo Canceladas', required=False, initial=0)
    monto_registro_efectivo = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_registro), label='Registrado Efectivo', required=False, initial=0)
    total_efectivo = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_total_efectivo), label='Total Efectivo', required=False, initial=0)
    rendicion_efectivo = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_monto_rendicion), label='Monto Rendicion Efectivo', required=False, initial=0)
    diferencia_efectivo = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_diferencia), label='Diferencia Registro/Rendicion Efectivo', required=False, initial=0)

# ==> TCs <==
    cantidad_operaciones_tcs_procesadas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TCs Procesadas', required=False, initial=0)
    cantidad_operaciones_tcs_pendientes = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TCs Pendientes', required=False, initial=0)
    cantidad_operaciones_tcs_canceladas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TCs Canceladas', required=False, initial=0)
    monto_registro_tcs = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_registro), label='Registrado TCs', required=False, initial=0)
    rendicion_tcs = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_monto_rendicion), label='Monto Rendicion TCs', required=False, initial=0)
    diferencia_tcs = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_diferencia), label='Diferencia Registro/Rendicion TCs', required=False, initial=0)

# ==> TDs <==
    cantidad_operaciones_tds_procesadas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TDs Procesadas', required=False, initial=0)
    cantidad_operaciones_tds_pendientes = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TDs Pendientes', required=False, initial=0)
    cantidad_operaciones_tds_canceladas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. TDs Canceladas', required=False, initial=0)
    monto_registro_tds = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_registro), label='Registrado TDs', required=False, initial=0)
    rendicion_tds = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_monto_rendicion), label='Monto Rendicion TDs', required=False, initial=0)
    diferencia_tds = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_diferencia), label='Diferencia Registro/Rendicion TDs', required=False, initial=0)

# ==> Otros Medios de Pago <==
    cantidad_operaciones_otros_medios_procesadas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Otros Medios Procesadas', required=False, initial=0)
    cantidad_operaciones_otros_medios_pendientes = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Otros Medios Pendientes', required=False, initial=0)
    cantidad_operaciones_otros_medios_canceladas = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_oper), label='Cant. Oper. Otros Medios Canceladas', required=False, initial=0)
    monto_registro_otros_medios = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_registro), label='Registrado Otros Medios', required=False, initial=0)
    rendicion_otros_medios = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_monto_rendicion), label='Monto Rendicion Otros Medios', required=False, initial=0)
    diferencia_otros_medios = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_monto_diferencia), label='Diferencia Registro/Rendicion Otros Medios', required=False, initial=0)

    total_diferencia = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                       label=mark_safe('<strong style="font-size: 14px;">Total Diferencia</strong>'),
                                       help_text='Si el Total Diferencia es negativo posee un sobrante.',
                                       required=False, initial=0)

    class Meta:
        model = CierreCaja
        fields = '__all__'
        # widgets = {
        #     'cantidad_operaciones_efectivo': forms.CharField(widget=forms.TextInput(attrs={'class':'hidden', 'readonly':'True', 'style': 'width: 40px;'}), label='Cant. Oper. Efectivo', required=False),
        #     'monto_registro_efectivo': forms.CharField(widget=forms.TextInput(attrs={'class':'hidden', 'readonly':'True', 'style': 'width: 400px;'}), label='Monto Registrado Efectivo', required=False),
        # }

    def __init__(self, *args, **kwargs):
        super(CierreCajaForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        cierre_caja = self.instance

        # if not cierre_caja.pk:
        #     usuario = Empleado.objects.get(usuario=self.request.user)
        #     # self.fields['apertura_caja'].queryset = aperturas
        #     self.fields['apertura_caja'].widget = CierreCajaRawIdWidget(rel=CierreCaja._meta.get_field('apertura_caja').rel, admin_site=site, attrs={'object': usuario})

        if cierre_caja.pk:
            # self.initial['apertura_caja'] = apertura.id
            # self.fields['apertura_caja'].queryset = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja='VIG')
            self.initial['cajero'] = cierre_caja.apertura_caja.cajero.nombre_completo
            self.initial['caja'] = cierre_caja.apertura_caja.caja
            self.initial['sector'] = cierre_caja.apertura_caja.sector
            self.initial['horario'] = cierre_caja.apertura_caja.horario
            self.initial['jornada'] = cierre_caja.apertura_caja.jornada
            self.initial['fecha_hora_apertura_caja'] = datetime.datetime.strftime(timezone.localtime(cierre_caja.apertura_caja.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')
            self.initial['monto_apertura'] = cierre_caja.apertura_caja.monto_apertura
            self.initial['estado_apertura_caja'] = cierre_caja.apertura_caja.get_estado_apertura_caja_display()

            if cierre_caja.apertura_caja.estado_apertura_caja == 'CER':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: green;'})
            elif cierre_caja.apertura_caja.estado_apertura_caja == 'VIG':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: orange;'})
            elif cierre_caja.apertura_caja.estado_apertura_caja == 'EXP':
                self.fields['estado_apertura_caja'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: red;'})

            if cierre_caja.apertura_caja.estado_apertura_caja in ('VIG', 'EXP'):
                cierre_caja.cantidad_total_operaciones_pendientes = cierre_caja.apertura_caja.get_cantidad_total_operaciones_pendientes()
                cierre_caja.cantidad_total_operaciones_canceladas = cierre_caja.apertura_caja.get_cantidad_total_operaciones_canceladas()
                cierre_caja.cantidad_operaciones_efectivo_procesadas = cierre_caja.apertura_caja.get_cantidad_operaciones_efectivo_procesadas()
                cierre_caja.cantidad_operaciones_efectivo_pendientes = cierre_caja.apertura_caja.get_cantidad_operaciones_efectivo_pendientes()
                cierre_caja.cantidad_operaciones_efectivo_canceladas = cierre_caja.apertura_caja.get_cantidad_operaciones_efectivo_canceladas()
                cierre_caja.monto_registro_efectivo = cierre_caja.apertura_caja.get_monto_registro_efectivo()

                cierre_caja.cantidad_operaciones_tcs_procesadas = cierre_caja.apertura_caja.get_cantidad_operaciones_tcs_procesadas()
                cierre_caja.cantidad_operaciones_tcs_pendientes = cierre_caja.apertura_caja.get_cantidad_operaciones_tcs_pendientes()
                cierre_caja.cantidad_operaciones_tcs_canceladas = cierre_caja.apertura_caja.get_cantidad_operaciones_tcs_canceladas()
                cierre_caja.monto_registro_tcs = cierre_caja.apertura_caja.get_monto_registro_tcs()

                cierre_caja.cantidad_operaciones_tds_procesadas = cierre_caja.apertura_caja.get_cantidad_operaciones_tds_procesadas()
                cierre_caja.cantidad_operaciones_tds_pendientes = cierre_caja.apertura_caja.get_cantidad_operaciones_tds_pendientes()
                cierre_caja.cantidad_operaciones_tds_canceladas = cierre_caja.apertura_caja.get_cantidad_operaciones_tds_canceladas()
                cierre_caja.monto_registro_tds = cierre_caja.apertura_caja.get_monto_registro_tds()

                cierre_caja.cantidad_operaciones_otros_medios_procesadas = cierre_caja.apertura_caja.get_cantidad_operaciones_otros_medios_procesadas()
                cierre_caja.cantidad_operaciones_otros_medios_pendientes = cierre_caja.apertura_caja.get_cantidad_operaciones_otros_medios_pendientes()
                cierre_caja.cantidad_operaciones_otros_medios_canceladas = cierre_caja.apertura_caja.get_cantidad_operaciones_otros_medios_canceladas()
                cierre_caja.monto_registro_otros_medios = cierre_caja.apertura_caja.get_monto_registro_otros_medios()

                cierre_caja.save()

                self.initial['cierre_caja.cantidad_total_operaciones_pendientes'] = cierre_caja.cantidad_total_operaciones_pendientes
                self.initial['cierre_caja.cantidad_total_operaciones_canceladas'] = cierre_caja.cantidad_total_operaciones_canceladas
                self.initial['cierre_caja.cantidad_operaciones_efectivo_procesadas'] = cierre_caja.cantidad_operaciones_efectivo_procesadas
                self.initial['cierre_caja.cantidad_operaciones_efectivo_pendientes'] = cierre_caja.cantidad_operaciones_efectivo_pendientes
                self.initial['cierre_caja.cantidad_operaciones_efectivo_canceladas'] = cierre_caja.cantidad_operaciones_efectivo_canceladas
                self.initial['cierre_caja.monto_registro_efectivo'] = cierre_caja.monto_registro_efectivo

                self.initial['cierre_caja.cantidad_operaciones_tcs_procesadas'] = cierre_caja.cantidad_operaciones_tcs_procesadas
                self.initial['cierre_caja.cantidad_operaciones_tcs_pendientes'] = cierre_caja.cantidad_operaciones_tcs_pendientes
                self.initial['cierre_caja.cantidad_operaciones_tcs_canceladas'] = cierre_caja.cantidad_operaciones_tcs_canceladas
                self.initial['cierre_caja.monto_registro_tcs'] = cierre_caja.monto_registro_tcs

                self.initial['cierre_caja.cantidad_operaciones_tds_procesadas'] = cierre_caja.cantidad_operaciones_tds_procesadas
                self.initial['cierre_caja.cantidad_operaciones_tds_pendientes'] = cierre_caja.cantidad_operaciones_tds_pendientes
                self.initial['cierre_caja.cantidad_operaciones_tds_canceladas'] = cierre_caja.cantidad_operaciones_tds_canceladas
                self.initial['cierre_caja.monto_registro_tds'] = cierre_caja.monto_registro_tds

                self.initial['cierre_caja.cantidad_operaciones_otros_medios_procesadas'] = cierre_caja.cantidad_operaciones_otros_medios_procesadas
                self.initial['cierre_caja.cantidad_operaciones_otros_medios_pendientes'] = cierre_caja.cantidad_operaciones_otros_medios_pendientes
                self.initial['cierre_caja.cantidad_operaciones_otros_medios_canceladas'] = cierre_caja.cantidad_operaciones_otros_medios_canceladas
                self.initial['cierre_caja.monto_registro_otros_medios'] = cierre_caja.monto_registro_otros_medios

    def clean(self):
        cleaned_data = super(CierreCajaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        cierre_caja = self.instance

        if cierre_caja:
            apertura = self.data.get('apertura_caja')
            try:
                cierres = CierreCaja.objects.filter(apertura_caja_id=apertura)
                if cierres.exists():
                    raise ValidationError({'apertura_caja': 'La Apertura de Caja seleccionada ya posee un Cierre de '
                                                            'Caja. Seleccione otra Apertura de Caja para completar '
                                                            'su Cierre de Caja.'})
            except ValueError:
                pass

            if cierre_caja.cantidad_total_operaciones_pendientes > 0:
                raise ValidationError({'cantidad_total_operaciones_pendientes': 'Posee Ventas Pendientes de ser '
                                                                                'procesadas. Procese las Ventas '
                                                                                'Pendientes o cancelelas y vuelva a '
                                                                                'intentar realizar el Cierre de Caja.'})

        return cleaned_data


class CambiarJornada(forms.Form):
    jornada = forms.ModelChoiceField(queryset=InicioJornada.objects.filter(estado_jornada='VIG'))


class InicioJornadaForm(forms.ModelForm):
    # mozo = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo__cargo__in=['MO', 'BM']), widget=ReadOnlySelect)
    # mozo = forms.ModelChoiceField(queryset=Empleado.objects.all(), widget=ReadOnlySelect)
    # mozo = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Mozo/Barman', required=False)
    nombre_mozo = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Nombre Mozo/Barman', required=False)
    # horario = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario', required=False)
    # sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
    #                          label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
    #                          required=False)
    duracion_jornada = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 60px;'}), label='Duracion Jornada', required=False)
    # fecha_hora_fin_jornada = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Fecha/hora Fin Jornada', required=False)

    class Meta:
        model = InicioJornada
        fields = '__all__'
        # exclude = ['mozo']
        # widgets = {'mozo': forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo__cargo__in=['MO', 'BM']), to_field_name='usuario', widget=ReadOnlySelect)}
        # widgets = {'mozo': forms.widgets.Select(attrs={'readonly': True, 'disabled': True})}

    def __init__(self, *args, **kwargs):
        super(InicioJornadaForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        jornada = self.instance

        if jornada.pk:
            # usuario = Empleado.objects.get(usuario=self.request.user)
            # self.initial['mozo'] = jornada.mozo
            self.initial['nombre_mozo'] = jornada.mozo.nombre_completo
            # self.initial['horario'] = jornada.mozo.horario
            # self.fields['mozo'].widget.attrs['readonly'] = True
            # self.fields['mozo'].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super(InicioJornadaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        jornada = self.instance

        if jornada:
            usuario = Empleado.objects.get(usuario=self.request.user)
            if usuario.usuario.is_superuser is True:
                pass
            elif usuario.cargo.cargo not in ('MO', 'BM'):
                raise ValidationError({'mozo': 'El Usuario no posee el cargo de Mozo/Barman. Modifique el cargo del '
                                               'Usuario y vuelva a intentarlo.'})

            jornadas = InicioJornada.objects.filter(mozo=usuario, estado_jornada__in=['VIG', 'EXP'])
            if jornadas.exists():
                raise ValidationError({'mozo': 'El Mozo/Barman ya posee un Inicio de Jornada vigente/expirado. '
                                               'Solo puede tener un Inicio de Jornada vigente/expirado.'})

            # if hasattr(self, 'disabled'):
            #     for x in self.disabled:
            #         data[x] = getattr(self.instance, x)
            # return data

            # self.initial['mozo'] = usuario
            # self.fields['mozo'] =
            # self.data.get('mozo', None)
            # self.cleaned_data['mozo']

        return cleaned_data

    # def clean_mozo(self):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     jornada = self.instance
    #
    #     if jornada.pk:
    #         return jornada.mozo
    #     else:
    #         return self.cleaned_data['mozo']


class FinJornadaForm(forms.ModelForm):
    nombre_mozo = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'width: 400px;'}), label='Nombre Mozo/Barman', required=False)
    # horario = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), label='Horario', required=False)
    # estado_jornada = forms.CharField(widget=forms.Select(attrs={'class':'hidden', 'readonly':'True', 'style': 'font-size: 15px; height: 30px; font-weight: bold; color: goldenrod;'}),
    #                                  label=mark_safe('<strong style="font-size: 14px;">Estado</strong>'),
    #                                  required=False)

    class Meta:
        model = FinJornada
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FinJornadaForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        jornada = self.instance

        if jornada and jornada.pk:
            # usuario = Empleado.objects.get(usuario=self.request.user)
            # self.initial['mozo'] = jornada.mozo
            self.initial['nombre_mozo'] = jornada.mozo.nombre_completo
            # self.initial['horario'] = jornada.mozo.horario
            # self.initial['estado_jornada'] = jornada.estado_jornada
            # self.fields['mozo'].widget.attrs['readonly'] = True
            # self.fields['mozo'].widget.attrs['disabled'] = True

            jornada.cantidad_pedidos_procesados = jornada.get_cantidad_pedidos_procesados()
            jornada.cantidad_pedidos_pendientes = jornada.get_cantidad_pedidos_pendientes()
            jornada.cantidad_pedidos_cancelados = jornada.get_cantidad_pedidos_cancelados()
            jornada.estado_jornada = jornada.get_estado_jornada()
            self.initial['estado_jornada'] = jornada.estado_jornada
            # self.fields['estado_jornada'].choices = jornada.get_estado_jornada_display()
            jornada.save()

            if jornada.estado_jornada == 'CER':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: green;'})
            elif jornada.estado_jornada == 'VIG':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: orange;'})
            elif jornada.estado_jornada == 'EXP':
                self.fields['estado_jornada'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; font-weight: bold; color: red;'})
            self.fields['estado_jornada'].widget.attrs['readonly'] = True
            self.fields['estado_jornada'].widget.attrs['disabled'] = True
            # self.fields['estado_jornada'].widget.attrs['required'] = False

    def clean(self):
        cleaned_data = super(FinJornadaForm, self).clean()

        # import pdb
        # pdb.set_trace()

        jornada = self.instance

        if jornada:
            if jornada.cantidad_pedidos_pendientes > 0:
                raise ValidationError('Posee Pedidos Pendientes de ser procesados. Procese los Pedidos Pendientes con '
                                      'el Cajero de su sector y vuelva a intentar realizar el Cierre de Jornada.')

        return cleaned_data