from django.contrib import admin

# Register your models here.
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.html import format_html

from .models import Pedido, PedidoDetalle, Venta, VentaDetalle, Comanda, AperturaCaja, CierreCaja
from personal.models import Empleado

# class PedidoDetalleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido')
#     list_filter = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']
#     search_fields = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']
from ventas.forms import AperturaCajaForm, VentaForm, PedidoForm, PedidoDetalleInlineForm


class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 0
    form = PedidoDetalleInlineForm
    # fields = ['producto_pedido', 'precio_producto_pedido']
    readonly_fields = ['fecha_pedido_detalle', 'procesado']
    raw_id_fields = ['producto_pedido']
    # verbose_name =
    # verbose_name_plural =

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        # if obj is not None and obj.estado_pedido == 'VIG' and self.procesado is False:
        #     return ['producto_pedido', 'precio_producto_pedido', 'cantidad_producto_pedido', 'total_producto_pedido',
        #             'fecha_pedido_detalle', 'procesado']
        # elif obj is not None and obj.estado_pedido == 'VIG' and self.procesado is True:
        #     return [i.name for i in self.model._meta.fields] + \
        #            [i.name for i in self.model._meta.many_to_many]
        if obj is not None and obj.estado_pedido.pedido_estado in ('PRO', 'CAN', 'ANU'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(PedidoDetalleInline, self).get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


class PedidoAdmin(admin.ModelAdmin):
    form = PedidoForm

    class Media:
        js = [
            'ventas/js/pedido.js'
        ]

    readonly_fields = ['numero_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_hora_pedido']  # Agregar 'total_pedido'

    raw_id_fields = ['reserva']

    filter_horizontal = ['mesa_pedido']

    fieldsets = [
        ('Numero Pedido', {'fields': ['numero_pedido']}),
        ('Datos de la Reserva', {'fields': ['reserva', 'id_cliente_reserva', 'cliente_reserva', 'monto_entrega_reserva']}),
        ('Datos del Pedido', {'fields': ['mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_hora_pedido', 'total_pedido']}),
        # ('Total', {'fields': []}),
    ]

    inlines = [PedidoDetalleInline]

    list_display = ['numero_pedido', 'reserva', 'mozo_pedido', 'colorea_estado_pedido', 'fecha_hora_pedido',
                    'total_pedido']
    list_filter = ['numero_pedido', 'mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_hora_pedido']
    search_fields = ['numero_pedido', 'mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_hora_pedido']

    def colorea_estado_pedido(self, obj):
        # color = 'black'
        if obj.estado_pedido.pedido_estado == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'ANU':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'VIG':
            color = 'indianred'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        return obj.estado_pedido.pedido_estado
    colorea_estado_pedido.short_description = 'Estado Pedido'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Al seleccionar la Reserva se deben cargar los datos del Monto de la Entrega y de las Mesas Reservadas. OK!
    # 2.1) Al guardar el Pedido se debe cambiar el estado de la Reserva a UTILIZADA en caso de que se haya utilizado una
    # 2.2) Al guardar el Pedido se debe descontar los productos solicitados del Stock.
    # 2.3) Al guardar el Pedido se debe modificar el estado de las Mesas seleccionadas a Ocupadas.
    # 4) Modificar el Estado del Pedido de acuerdo a las acciones que se realicen con el mismo. Por de pronto el campo
    # estado_pedido queda como readonly.
    # 5) Se debe restar el "monto_entrega_reserva" al "total_pedido" en caso de utilizar una Reserva.
    # 6) Analizar la manera de seguir agregando productos a un mismo Pedido y como funcionara esta pantalla en ese caso.
    # 7) Se debe poder cancelar o anular el Pedido. Se podria agregar un boton de "Cancelar" que requiera el ingreso de
    # un motivo de cancelacion o anulacion. Al anularse o cancelarse un Pedido se deben sumar nuevamente al Stock los
    # Productos solicitados y que ya fueron descontados.
    # 8) Los pedidos con estado "Procesado" y "Cancelado" no deben poder ser modificados.
    # 9) Calcular automaticamente el campo "total_pedido" de acuerdo a los valores de "total_producto_pedido" para cada
    # Producto del detalle. En caso de eliminar un Producto se debe restar al campo "total_pedido"
    # 10) mozo_pedido: Debe ser el usuario con el cual se esta registrando el Pedido, no se debe poder seleccionar el
    # usuario. OK!

    def save_model(self, request, obj, form, change):
        # if obj.reserva:

        if getattr(obj, 'mozo_pedido', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.mozo_pedido = Empleado.objects.get(usuario_id=request.user)
        super(PedidoAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_pedido.pedido_estado == 'VIG' and obj.reserva is not None:
            return self.readonly_fields + ['reserva']
        elif obj is not None and obj.estado_pedido in ('PRO', 'CAN', 'ANU'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(PedidoAdmin, self).get_readonly_fields(request, obj)

    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #
    #     extra_context['show_button'] = False
    #     # if object_id is not None:
    #     #     apertura_caja_actual = AperturaCaja.objects.get(pk=object_id)
    #     #     extra_context['show_button'] = apertura_caja_actual.estado_apertura_caja not in ('VIG', 'CER')
    #     return super(PedidoAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     form = super(ComandaAdmin, self).get_form(request, obj=obj, **kwargs)
    #     usuario = Empleado.objects.get(usuario=request.user)
    #     form.base_fields['cajero'].initial = usuario
    #     form.base_fields['horario'].initial = usuario.horario
    #     form.base_fields['cajero'].widget.attrs['readonly'] = True
    #     form.base_fields['horario'].widget.attrs['readonly'] = True
    #     # form.base_fields['cajero'].widget.attrs['disabled'] = True
    #     # form.base_fields['horario'].widget.attrs['disabled'] = True
    #     form.request = request
    #     return form

    def has_delete_permission(self, request, obj=None):
        return False


class VentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    extra = 0
    # form =
    raw_id_fields = ['producto_venta']
    # verbose_name =
    # verbose_name_plural =


class VentaAdmin(admin.ModelAdmin):
    form = VentaForm

    class Media:
        js = [
            'ventas/js/venta.js'
        ]

    readonly_fields = ['empresa', 'numero_factura_venta', 'fecha_hora_venta', 'estado_venta']

    raw_id_fields = ['cliente_factura', 'numero_pedido']

    fieldsets = [
        ('Datos Facturacion', {'fields': [('empresa', 'timbrado', 'fecha_limite_vigencia_timbrado'),
                                          'numero_factura_venta',
                                          ('apertura_caja', 'caja', 'cajero', 'horario', 'fecha_apertura_caja'),
                                          'fecha_hora_venta']}),
        ('Pedido', {'fields': ['numero_pedido', 'total_pedido']}),
        ('Reserva/Cliente', {'fields': ['posee_reserva', 'entrega_reserva', 'cliente_factura']}),
        ('Venta', {'fields': ['forma_pago', 'estado_venta', 'total_venta']})
    ]

    inlines = [VentaDetalleInline]

    list_display = ['id', 'numero_factura_venta', 'cliente_factura', 'fecha_hora_venta',  # 'apertura_caja',
                    'numero_pedido', 'forma_pago', 'total_venta', 'estado_venta']
    list_filter = ['id', 'numero_factura_venta', 'cliente_factura', 'fecha_hora_venta',  # 'apertura_caja',
                    'numero_pedido', 'forma_pago', 'total_venta', 'estado_venta']
    search_fields = ['id', 'numero_factura_venta', 'cliente_factura__nombre_completo', 'fecha_hora_venta',  # 'apertura_caja',
                    'numero_pedido', 'forma_pago', 'total_venta', 'estado_venta']

    def colorea_estado_venta(self, obj):
        # color = 'black'
        if obj.estado_venta.venta_estado == 'CON':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'ANU':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'PEN':
            color = 'indianred'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        return obj.estado_venta.venta_estado
    colorea_estado_venta.short_description = 'Estado Venta'

    # def save_model(self, request, obj, form, change):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     apertura_caja_actual = obj
    #     apertura_caja_actual.estado_apertura_caja = 'VIG'
    #     caja = apertura_caja_actual.caja
    #     caja.estado_caja = 'ABI'
    #     caja.save()
    #
    #     super(AperturaCajaAdmin, self).save_model(request, obj, form, change)
    #
    # def get_readonly_fields(self, request, obj=None):
    #     if obj is not None and obj.estado_apertura_caja in ('VIG', 'CER'):
    #         return [i.name for i in self.model._meta.fields] + \
    #                [i.name for i in self.model._meta.many_to_many]
    #     else:
    #         return super(AperturaCajaAdmin, self).get_readonly_fields(request, obj)
    #
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #
    #     extra_context['show_button'] = True
    #     if object_id is not None:
    #         apertura_caja_actual = AperturaCaja.objects.get(pk=object_id)
    #         extra_context['show_button'] = apertura_caja_actual.estado_apertura_caja not in ('VIG', 'CER')
    #     return super(AperturaCajaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(VentaAdmin, self).get_form(request, obj=obj, **kwargs)
        # usuario = Empleado.objects.get(usuario=request.user)
        # form.base_fields['cajero'].initial = usuario
        # form.base_fields['horario'].initial = usuario.horario
        form.base_fields['apertura_caja'].widget.attrs['readonly'] = True
        # form.base_fields['cajero'].widget.attrs['disabled'] = True
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False


class ComandaAdmin(admin.ModelAdmin):
    # form =

    readonly_fields = []

    raw_id_fields = ['producto_a_elaborar']

    fieldsets = [
        ('Datos Comanda', {'fields': ['producto_a_elaborar', 'area_encargada', 'fecha_hora_pedido_comanda',
                                      'tiempo_estimado_elaboracion']}),
        ('Estado', {'fields': ['estado_comanda', 'fecha_hora_procesamiento_comanda']}),
    ]

    list_display = ['producto_a_elaborar', 'area_encargada', 'fecha_hora_pedido_comanda', 'tiempo_estimado_elaboracion',
                    'colorea_estado_comanda', 'fecha_hora_procesamiento_comanda']
    list_filter = ['producto_a_elaborar', 'area_encargada', 'fecha_hora_pedido_comanda', 'estado_comanda',
                   'fecha_hora_procesamiento_comanda']
    search_fields = ['producto_a_elaborar', 'area_encargada', 'fecha_hora_pedido_comanda', 'estado_comanda',
                     'fecha_hora_procesamiento_comanda']

    def colorea_estado_comanda(self, obj):
        # color = 'black'
        if obj.estado_comanda == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        elif obj.estado_comanda == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        elif obj.estado_comanda == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        return obj.estado_comanda
    colorea_estado_comanda.short_description = 'Estado Comanda'

    # def save_model(self, request, obj, form, change):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     apertura_caja_actual = obj
    #     apertura_caja_actual.estado_apertura_caja = 'VIG'
    #     caja = apertura_caja_actual.caja
    #     caja.estado_caja = 'ABI'
    #     caja.save()
    #
    #     super(ComandaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:  # and obj.estado_apertura_caja in ('VIG', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(ComandaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = False
        # if object_id is not None:
        #     apertura_caja_actual = AperturaCaja.objects.get(pk=object_id)
        #     extra_context['show_button'] = apertura_caja_actual.estado_apertura_caja not in ('VIG', 'CER')
        return super(ComandaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     form = super(ComandaAdmin, self).get_form(request, obj=obj, **kwargs)
    #     usuario = Empleado.objects.get(usuario=request.user)
    #     form.base_fields['cajero'].initial = usuario
    #     form.base_fields['horario'].initial = usuario.horario
    #     form.base_fields['cajero'].widget.attrs['readonly'] = True
    #     form.base_fields['horario'].widget.attrs['readonly'] = True
    #     # form.base_fields['cajero'].widget.attrs['disabled'] = True
    #     # form.base_fields['horario'].widget.attrs['disabled'] = True
    #     form.request = request
    #     return form

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AperturaCajaAdmin(admin.ModelAdmin):
    form = AperturaCajaForm

    # class Media:
    #     js = [
    #         'ventas/js/apertura_caja.js'
    #     ]

    # formfield_overrides = []

    readonly_fields = ['fecha_apertura_caja', 'fecha_hora_registro_apertura_caja',
                       'estado_apertura_caja']

    raw_id_fields = ['caja', ]

    fieldsets = [
        ('Datos Apertura', {'fields': ['cajero', 'horario', 'fecha_apertura_caja', 'caja']}),
        ('Monto Apertura', {'fields': ['monto_apertura']}),
        ('Otros datos', {'fields': ['estado_apertura_caja', 'fecha_hora_registro_apertura_caja']}),
    ]

    list_display = ['id', 'caja', 'cajero', 'horario', 'fecha_apertura_caja', 'monto_apertura',
                    'colorea_estado_apertura_caja', 'fecha_hora_registro_apertura_caja']
    list_display_links = ['caja']
    list_filter = ['id', 'caja', 'cajero', 'horario', 'fecha_apertura_caja', 'estado_apertura_caja']
    search_fields = ['caja__numero_caja', 'cajero__usuario__username', 'horario__horario', 'fecha_apertura_caja',
                     'monto_apertura', 'estado_apertura_caja']

    def colorea_estado_apertura_caja(self, obj):
        # color = 'black'
        if obj.estado_apertura_caja == 'VIG':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_apertura_caja_display()))
        elif obj.estado_apertura_caja == 'CER':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_apertura_caja_display()))
        return obj.estado_apertura_caja
    colorea_estado_apertura_caja.short_description = 'Estado Apertura Caja'

    def save_model(self, request, obj, form, change):

        import pdb
        pdb.set_trace()

        apertura_caja_actual = obj
        apertura_caja_actual.estado_apertura_caja = 'VIG'
        caja = apertura_caja_actual.caja
        caja.estado_caja = 'ABI'
        caja.save()

        super(AperturaCajaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_apertura_caja in ('VIG', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(AperturaCajaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            apertura_caja_actual = AperturaCaja.objects.get(pk=object_id)
            extra_context['show_button'] = apertura_caja_actual.estado_apertura_caja not in ('VIG', 'CER')
        return super(AperturaCajaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        import pdb
        pdb.set_trace()

        form = super(AperturaCajaAdmin, self).get_form(request, obj=obj, **kwargs)
        if obj is None:
            usuario = Empleado.objects.get(usuario=request.user)
            form.base_fields['cajero'].initial = usuario
            form.base_fields['horario'].initial = usuario.horario
            form.base_fields['cajero'].widget.attrs['readonly'] = True
            form.base_fields['horario'].widget.attrs['readonly'] = True
            # form.base_fields['cajero'].widget.attrs['disabled'] = True
            # form.base_fields['horario'].widget.attrs['disabled'] = True
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False


class CierreCajaAdmin(admin.ModelAdmin):
    # form =

    readonly_fields = ['fecha_hora_registro_cierre_caja']

    raw_id_fields = ['apertura_caja']

    fieldsets = [
        ('Datos Apertura', {'fields': ['apertura_caja']}),
        ('Otros datos', {'fields': ['fecha_hora_registro_cierre_caja']}),
        ('Rendicion', {'fields': [('monto_registro_efectivo', 'rendicion_efectivo', 'diferencia_efectivo'),
                                  ('monto_registro_tcs', 'rendicion_tcs', 'diferencia_tcs'),
                                  ('monto_registro_tds', 'rendicion_tds', 'diferencia_tds'),
                                  ('monto_registro_otros_medios', 'rendicion_otros_medios', 'diferencia_otros_medios')]}),
    ]

    list_display = ['id', 'apertura_caja', 'fecha_hora_registro_cierre_caja']
    list_filter = ['id', 'apertura_caja', 'fecha_hora_registro_cierre_caja']
    # search_fields = ['caja__numero_caja', 'monto_apertura', 'cajero__usuario__username', 'fecha_hora_apertura_caja']


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Comanda, ComandaAdmin)
admin.site.register(AperturaCaja, AperturaCajaAdmin)
admin.site.register(CierreCaja, CierreCajaAdmin)
# admin.site.register(MovimientoCaja)
