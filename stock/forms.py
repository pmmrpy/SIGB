import pdb
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe
from bar.models import UnidadMedidaProducto, Deposito
from .models import Producto, ProductoCompuesto, MovimientoStock  # PrecioVentaProducto
from dal import autocomplete
from stock.models import *

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO_monto = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_monto['style'] += 'width: 150px;'
ATTR_NUMERICO_cantidad_prod = ATTR_NUMERICO.copy()
ATTR_NUMERICO_cantidad_prod['style'] += 'width: 100px;'
ATTR_NUMERICO_cantidad_prod['step'] = '0.001'
ATTR_NUMERICO_RO_RESALTADO_cantidad = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_cantidad['style'] += 'width: 100px;'
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'
ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'
ATTR_NUMERICO_RO_cant_exist = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_cant_exist['style'] += 'width: 50px;'

# Restringir la carga de un mismo producto varias veces
# Producto.precio_venta = Debe ser el ultimo precio definido en PrecioProducto, se debe validar por la fecha.as


# class PrecioVentaProductoForm(forms.ModelForm):
#     class Meta:
#         model = PrecioVentaProducto
#         fields = '__all__'
#         localized_fields = ('precio_venta',)

class ProductoForm(forms.ModelForm):

    precio_compra_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                             label='Precio Compra Sugerido', required=False,
                                             help_text='Este valor se calcula promediando el Costo de Compra del '
                                                       'Producto en los ultimos 30 dias.')
    precio_venta_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                            label='Precio Venta Sugerido', required=False,
                                            help_text='Precio de Venta sugerido calculado a partir del Precio Compra '
                                                      'Sugerido por el Porcentaje de Ganancia. Cuando el Producto es '
                                                      'registrado por primera vez se calcula el Precio de Compra por '
                                                      'el Porcentaje de Ganancia ingresados.')

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'producto': forms.TextInput(attrs={'style': 'width: 500px;'}),
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        # instance = getattr(self, 'instance', None)

        # import pdb
        # pdb.set_trace()

        producto = self.instance

        if producto.pk:  # and self.instance.pk:
            self.initial['precio_compra_sugerido'] = producto.get_precio_compra_sugerido()
            # self.initial['precio_venta_sugerido'] = self.instance.get_precio_venta_sugerido()
            # self.instance.save()
            # if self.fields['tipo_producto'] == 'IN':
            #     self.fields['porcentaje_ganancia'].widgets.attrs['readonly'] = True
            #     self.fields['precio_venta_sugerido'].widgets.attrs['readonly'] = True
            # elif self.fields['tipo_producto'] == 'VE':
            #     self.fields['porcentaje_ganancia'].widgets.attrs['readonly'] = False
            #     self.fields['precio_venta_sugerido'].widgets.attrs['readonly'] = False


class ProductoCompuestoDetalleInlineForm(forms.ModelForm):

    # unidad_medida_contenido = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'True', 'style': 'width: 100px;'}), label='Un. Med. Cont.', required=False)
    # contenido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_cantidad), label='Cant. Contenido', required=False)
    # costo_unidad_medida = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_monto), label='Costo por Un. Medida', required=False)
    # cantidad_producto = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_cantidad_prod), label='Cant. Producto', required=False)
    # total_costo = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_monto), label='Total Costo', required=False)

    class Meta:
        model = ProductoCompuestoDetalle
        fields = '__all__'
        # widgets = {
        #     # 'producto': forms.TextInput(attrs={'style': 'width: 500px;'}),
        #     # 'unidad_medida_insumo': forms.TextInput(attrs={'readonly':'True', 'style': 'width: 150px;'}),
        #     # 'costo_promedio_insumo': forms.TextInput(attrs={'readonly':'True'}),
        #     # 'total_costo': forms.TextInput(attrs={'readonly':'True'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(ProductoCompuestoDetalleInlineForm, self).__init__(*args, **kwargs)
    #
    #     detalle_prod_comp = self.instance
    #
    #     if not detalle_prod_comp.pk:
    #         # self.fields['unidad_medida_contenido'].queryset = UnidadMedidaProducto.objects.filter(pk=detalle_prod_comp.unidad_medida_contenido_id)
    #         self.fields['unidad_medida_insumo'].widget.attrs.update({'style': 'width: 150px;'})
    #         self.fields['unidad_medida_insumo'].widget.attrs['readonly'] = True
    #
    #     elif detalle_prod_comp.pk:
    #         # self.fields['unidad_medida_contenido'].queryset = UnidadMedidaProducto.objects.filter(pk=detalle_prod_comp.unidad_medida_contenido_id)
    #         self.fields['unidad_medida_insumo'].widget.attrs.update({'style': 'width: 150px;'})
    #         self.fields['unidad_medida_insumo'].widget.attrs['readonly'] = True


class ProductoCompuestoForm(forms.ModelForm):

    producto = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 500px;'}), label='Nombre del Producto', required=False,
                               help_text='Ingrese el nombre o descripcion del Producto.')
    costo_elaboracion = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO), label='Costo de Elaboracion', required=False)
    precio_venta_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2), label='Precio Venta Sugerido', required=False,
                                            help_text='Precio de Venta sugerido calculado a partir del Costo de '
                                                      'Elaboracion por el Porcentaje de Ganancia.')
    # insumos_disponibles = forms.BooleanField(label='Insumos disponibles?', required=False)

    class Meta:
        model = ProductoCompuesto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }

    def __init__(self, *args, **kwargs):
        super(ProductoCompuestoForm, self).__init__(*args, **kwargs)

        # instance = getattr(self, 'instance', None)

        # import pdb
        # pdb.set_trace()

        producto_compuesto = self.instance

        if producto_compuesto.pk:  # and self.instance.pk:
            self.initial['precio_venta_sugerido'] = producto_compuesto.get_precio_venta_sugerido_producto_compuesto()
            # self.initial['insumos_disponibles'] = producto_compuesto.get_insumos_disponibles_producto_compuesto()


class InsumoForm(forms.ModelForm):
    costo_promedio = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), required=False, initial=0,
                                     label='Costo Promedio por Unidad',
                                     help_text='Promedio de los Precios de Compra de los Productos integrantes.')
    cantidad_existente = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), required=False, initial=0,
                                         label='Cantidad Existente',
                                         help_text='Cantidad existente del Insumo calculado a partir de las cantidades '
                                                   'existentes de los Productos integrantes.')
    
    class Meta:
        model = Insumo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InsumoForm, self).__init__(*args, **kwargs)

        insumo = self.instance

        if insumo.pk:
            self.fields['costo_promedio'].initial = insumo.get_costo_promedio_por_unidad()
            # self.fields['costo_promedio'].widget.attrs['readonly'] = True
            self.fields['cantidad_existente'].initial = insumo.get_cantidad_existente_insumo()


class TransferenciaStockForm(forms.ModelForm):
    
    # cant_exist_dce = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Central.', required=False, initial=0)
    # cant_exist_dbp = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Bar. Pr.', required=False, initial=0)
    # cant_exist_dba = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Arriba', required=False, initial=0)
    # cant_exist_dco = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Cocina', required=False, initial=0)
    # cant_exist_dbi = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Barrita', required=False, initial=0)
    # cant_total_existente = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Total Existente', required=False, initial=0)

    class Meta:
        model = TransferenciaStock
        fields = '__all__'
        # widgets = {
        #
        # }
        
    # def __init__(self, *args, **kwargs):
    #     super(TransferenciaStockForm, self).__init__(*args, **kwargs)
    #
    #     transferencia = self.instance
    #
    #     if transferencia.pk:
    #         if transferencia.producto_transferencia is not None:
    #             try:
    #                 stock = InventarioDeposito.objects.get(pk=transferencia.producto_transferencia.id)
    #             except InventarioDeposito.DoesNotExist:
    #                 stock = None
    #
    #             self.initial['cant_exist_dce'] = stock.cant_exist_dce or 0
    #             self.initial['cant_exist_dbp'] = stock.cant_exist_dbp or 0
    #             self.initial['cant_exist_dba'] = stock.cant_exist_dba or 0
    #             self.initial['cant_exist_dco'] = stock.cant_exist_dco or 0
    #             self.initial['cant_exist_dbi'] = stock.cant_exist_dbi or 0
    #             self.initial['cant_total_existente'] = stock.cant_existente or 0

    def clean(self):
        cleaned_data = super(TransferenciaStockForm, self).clean()

        # import pdb
        # pdb.set_trace()

        transferencia = self.instance

        if '_save' in self.request.POST:
            if not transferencia.pk:
                if hasattr(self.cleaned_data, 'deposito_destino_transferencia') is True and hasattr(self.cleaned_data, 'deposito_origen_transferencia') is True \
                        and self.cleaned_data['deposito_destino_transferencia'] == self.cleaned_data['deposito_origen_transferencia']:
                    raise ValidationError({'deposito_destino_transferencia': 'El Deposito Destino no puede ser el mismo '
                                                                             'que el Deposito Origen. Seleccione otro '
                                                                             'Deposito Destino.'})

        # 2) Validar que el "deposito_proveedor_transferencia" disponga de la cantidad suficiente del producto solicitado
        # para que se pueda realizar la transferencia al "deposito_solicitante_transferencia".

        return cleaned_data


class TransferenciaStockDetalleFormSet(BaseInlineFormSet):

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request
        for form in self.forms:
            form.request = request


class TransferenciaStockDetalleInlineForm(forms.ModelForm):

    cant_exist_dce = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Central.', required=False, initial=0)
    cant_exist_dbp = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Bar. Pr.', required=False, initial=0)
    cant_exist_dba = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Arriba', required=False, initial=0)
    cant_exist_dco = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Cocina', required=False, initial=0)
    cant_exist_dbi = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Exist. Dep. Barrita', required=False, initial=0)
    cant_total_existente = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist), label='Cant. Total Existente', required=False, initial=0)

    class Meta:
        model = TransferenciaStockDetalle
        fields = '__all__'
        widgets = {
            'unidad_medida': forms.Select(attrs={'style': 'width: 120px;'}),
            'cantidad_producto_transferencia': forms.TextInput(attrs=ATTR_NUMERICO_cantidad_prod),
        }

    def __init__(self, *args, **kwargs):
        super(TransferenciaStockDetalleInlineForm, self).__init__(*args, **kwargs)

        transferencia = self.instance

        # self.fields['unidad_medida'].widget.attrs['style'] = 'width: 50px;'
        # self.fields['cantidad_producto_transferencia'].widget.attrs['style'] = 'width: 50px;'

        if transferencia.pk:
            if transferencia.producto_transferencia is not None:
                try:
                    stock = InventarioDeposito.objects.get(pk=transferencia.producto_transferencia.id)
                except InventarioDeposito.DoesNotExist:
                    stock = None

                self.initial['cant_exist_dce'] = stock.cant_exist_dce or 0
                self.initial['cant_exist_dbp'] = stock.cant_exist_dbp or 0
                self.initial['cant_exist_dba'] = stock.cant_exist_dba or 0
                self.initial['cant_exist_dco'] = stock.cant_exist_dco or 0
                self.initial['cant_exist_dbi'] = stock.cant_exist_dbi or 0
                self.initial['cant_total_existente'] = stock.cant_existente or 0

    def clean(self):
        cleaned_data = super(TransferenciaStockDetalleInlineForm, self).clean()

        # import pdb
        # pdb.set_trace()

        detalle_transferencia = self.instance

        if '_save' in self.request.POST or '_continue' in self.request.POST:
            # 2) Validar que el "deposito_proveedor_transferencia" disponga de la cantidad suficiente del producto solicitado
            # para que se pueda realizar la transferencia al "deposito_solicitante_transferencia".

            # Validar que cantidad_producto_transferencia no sea superior que la cantidad disponible en el deposito_proveedor
            if 'producto_transferencia' in self.cleaned_data and self.cleaned_data['producto_transferencia'] is not None and self.cleaned_data['producto_transferencia'] != '':
                try:
                    stock = InventarioDeposito.objects.get(pk=self.cleaned_data['producto_transferencia'].id)
                except InventarioDeposito.DoesNotExist:
                    stock = None

                id_deposito_solicitante = ''
                id_deposito_proveedor = ''
                s = ''
                p = ''

                if detalle_transferencia.pk:
                    id_deposito_solicitante = detalle_transferencia.transferencia.deposito_destino_transferencia.id
                    id_deposito_proveedor = detalle_transferencia.transferencia.deposito_origen_transferencia.id
                elif not detalle_transferencia.pk:
                    id_deposito_solicitante = self.request.POST.get('deposito_destino_transferencia', '')
                    id_deposito_proveedor = self.request.POST.get('deposito_origen_transferencia', '')

                if id_deposito_solicitante is not None and id_deposito_solicitante != '':
                    deposito_solicitante = Deposito.objects.get(pk=id_deposito_solicitante)
                    s = str(deposito_solicitante.deposito)
                    s = s.lower()

                if id_deposito_proveedor is not None and id_deposito_proveedor != '':
                    deposito_proveedor = Deposito.objects.get(pk=id_deposito_proveedor)
                    p = str(deposito_proveedor.deposito)
                    p = p.lower()

                if stock is not None and 'cantidad_producto_transferencia' in self.cleaned_data \
                        and self.cleaned_data['cantidad_producto_transferencia'] > getattr(stock, 'cant_exist_' + p):
                    raise ValidationError({'cantidad_producto_transferencia': 'La cantidad a transferir del Producto no '
                                                                              'puede ser mayor que la cantidad disponible '
                                                                              'en el Deposito Proveedor.'})

        return cleaned_data


class AjusteStockForm(forms.ModelForm):

    class Meta:
        model = AjusteStock
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AjusteStockForm, self).clean()

        # import pdb
        # pdb.set_trace()

        ajuste = self.instance

        if '_continue' in self.request.POST or '_save' in self.request.POST:
            if not ajuste.pk:
                if hasattr(self.cleaned_data, 'deposito') is True and self.cleaned_data['deposito'] is not None and self.cleaned_data['deposito'] != '' \
                        and AjusteStock.objects.filter(deposito=self.cleaned_data['deposito'], estado_ajuste__estado_ajuste_stock='PEN').exists():
                    raise ValidationError({'deposito': ('Ya existe un Ajuste de Inventario pendiente para el Deposito "%s". Seleccione otro Deposito.' % self.cleaned_data['deposito'])})

        return cleaned_data


class AjusteStockDetalleFormSet(BaseInlineFormSet):

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request
        for form in self.forms:
            form.request = request


class AjusteStockDetalleInlineForm(forms.ModelForm):

    class Meta:
        model = AjusteStockDetalle
        fields = '__all__'
        # widgets = {
        #     # 'unidad_medida': forms.Select(attrs={'style': 'width: 120px;'}),
        #     # 'cantidad_existente_producto': forms.TextInput(attrs=ATTR_NUMERICO_RO_cant_exist),
        #     # 'cantidad_ajustar_producto': forms.TextInput(attrs=ATTR_NUMERICO_cantidad_prod),
        #     # 'motivo_ajuste': forms.TextInput(attrs={'style': 'width: 200px;'}),
        # }

    def __init__(self, *args, **kwargs):
        super(AjusteStockDetalleInlineForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        ajuste_stock = self.instance

        if ajuste_stock.pk and ajuste_stock.ajuste_stock.estado_ajuste.estado_ajuste_stock == 'PEN':

            try:
                producto_stock_deposito = StockDepositoAjusteInventario.objects.get(id=ajuste_stock.producto_ajuste.id, deposito_id=ajuste_stock.ajuste_stock.deposito.id)
            except StockDepositoAjusteInventario.DoesNotExist:
                producto_stock_deposito = None

            if producto_stock_deposito is not None:
                ajuste_stock.id = ajuste_stock.id
                ajuste_stock.producto_ajuste_id = producto_stock_deposito.id
                ajuste_stock.unidad_medida_id = producto_stock_deposito.get_unidad_medida_id_inventario_deposito()
                ajuste_stock.cantidad_existente_producto = producto_stock_deposito.cantidad_existente
                ajuste_stock.save()
                self.initial['unidad_medida'] = ajuste_stock.unidad_medida
                self.initial['cantidad_existente_producto'] = ajuste_stock.cantidad_existente_producto

            elif producto_stock_deposito is None:
                ajuste_stock.delete()

            if ajuste_stock.ajustar is False:
                self.initial['cantidad_ajustar_producto'] = ''
                # self.fields['cantidad_ajustar_producto'].widget.attrs = ATTR_NUMERICO_cantidad_prod
                self.fields['cantidad_ajustar_producto'].widget.attrs['readonly'] = True
                self.initial['motivo_ajuste'] = ''
                self.fields['motivo_ajuste'].widget.attrs['style'] = 'width: 200px;'
                self.fields['motivo_ajuste'].widget.attrs['readonly'] = True
            elif ajuste_stock.ajustar is True:
                # self.fields['cantidad_ajustar_producto'].widget.attrs = ATTR_NUMERICO_cantidad_prod
                self.fields['cantidad_ajustar_producto'].widget.attrs['readonly'] = False
                self.fields['motivo_ajuste'].widget.attrs['style'] = 'width: 200px;'
                self.fields['motivo_ajuste'].widget.attrs['readonly'] = False

    def clean(self):
        cleaned_data = super(AjusteStockDetalleInlineForm, self).clean()

        # import pdb
        # pdb.set_trace()

        ajuste_stock = self.instance

        if ajuste_stock.pk:
            try:
                producto_stock_deposito = StockDepositoAjusteInventario.objects.get(id=ajuste_stock.producto_ajuste.id, deposito_id=ajuste_stock.ajuste_stock.deposito.id)
            except StockDepositoAjusteInventario.DoesNotExist:
                producto_stock_deposito = None

            if '_save' in self.request.POST or '_continue' in self.request.POST:
                if self.cleaned_data['ajustar'] is True:
                    # if hasattr(self.cleaned_data, 'cantidad_ajustar_producto') is False or hasattr(self.cleaned_data, 'cantidad_ajustar_producto') is True \
                    #         and self.cleaned_data['cantidad_ajustar_producto'] is None or hasattr(self.cleaned_data, 'cantidad_ajustar_producto') is True \
                    #         and self.cleaned_data['cantidad_ajustar_producto'] == '':
                    if self.cleaned_data['cantidad_ajustar_producto'] is None or self.cleaned_data['cantidad_ajustar_producto'] == '':
                        raise ValidationError({'cantidad_ajustar_producto': 'Debe ingresar un valor para la Cantidad a '
                                                                            'Ajustar del Producto.'})

                    # elif hasattr(self.cleaned_data, 'motivo_ajuste') is False or hasattr(self.cleaned_data, 'motivo_ajuste') is True \
                    #         and self.cleaned_data['motivo_ajuste'] is None or hasattr(self.cleaned_data, 'motivo_ajuste') is True \
                    #         and self.cleaned_data['motivo_ajuste'] == '':
                    if self.cleaned_data['motivo_ajuste'] is None or self.cleaned_data['motivo_ajuste'] == '':
                        raise ValidationError({'motivo_ajuste': 'Debe ingresar un valor para el Motivo de Ajuste.'})

                    if ajuste_stock.cantidad_existente_producto != producto_stock_deposito.cantidad_existente:
                        raise ValidationError({'cantidad_ajustar_producto': 'La cantidad existente del Producto a ajustar '
                                                                            'tuvo una variacion, corrobore los datos del '
                                                                            'Ajuste de Inventario antes de Confirmarlo.'})

                    elif ajuste_stock.cantidad_existente_producto == self.cleaned_data['cantidad_ajustar_producto']:
                        raise ValidationError({'cantidad_ajustar_producto': 'La cantidad a ajustar del Producto no puede '
                                                                            'ser la misma que la cantidad existente. '
                                                                            'Modifique la cantidad a ajustar y vuelva a '
                                                                            'confirmar el Ajuste de Invetario.'})
        return cleaned_data