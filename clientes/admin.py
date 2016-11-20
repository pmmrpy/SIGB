import datetime
from calendarium.models import Event, EventCategory
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from bar.models import ReservaEstado
from clientes.forms import ClienteForm, ReservaForm, ClienteTelefonoForm, ClienteDocumentoForm
from .models import Cliente, ClienteTelefono, Reserva, ClienteDocumento  # TelefonoMovilCliente, CalendarioReserva
from personal.models import Empleado
# from ajax_select import make_ajax_form

# Register your models here.


class ClienteDocumentoInline(admin.TabularInline):
    model = ClienteDocumento
    extra = 0
    form = ClienteDocumentoForm
    readonly_fields = ['digito_verificador']
    min_num = 1
    verbose_name = 'Documento del Cliente'
    verbose_name_plural = 'Documentos del Cliente'


class ClienteTelefonoInline(admin.TabularInline):
    model = ClienteTelefono
    extra = 0
    min_num = 1
    form = ClienteTelefonoForm
    verbose_name = 'Telefono del Cliente'
    verbose_name_plural = 'Telefonos del Cliente'


class ClienteAdmin(admin.ModelAdmin):

    form = ClienteForm

    class Media:
        js = [
            'clientes/js/rango.js',
            'clientes/js/cliente.js'
        ]
        css = {
            'all': ('clientes/css/cliente.css',)
        }

    fieldsets = [
        ('Nombres y Apellidos', {'fields': ['nombres', 'apellidos']}),
        ('Informacion Personal', {'fields': ['fecha_nacimiento', 'sexo', 'direccion', 'pais', 'ciudad', 'email']}),
        # ('Sexo', {'fields': ['sexo']}),
        # ('Direccion / Pais / Ciudad', {'fields': ['direccion', ('pais', 'ciudad')]}),
        # ('Telefonos', {'fields': ['telefono', 'telefono_movil']}),
        # ('Email', {'fields': ['email']}),  # , 'classes': ['collapse']
    ]
    inlines = [ClienteTelefonoInline, ClienteDocumentoInline]

    list_display = ['id', 'upper_case_name', 'direccion', 'pais', 'ciudad', 'fecha_nacimiento', 'email']
    list_display_links = ['upper_case_name']
    list_filter = ['nombres', 'apellidos', 'pais', 'ciudad', 'fecha_nacimiento', 'email']
    # search_fields = ['id', 'nombres', 'apellidos', 'direccion', 'pais', 'ciudad', 'email']
    search_fields = ['id', 'nombres', 'apellidos', 'direccion', 'pais__pais', 'ciudad__ciudad', 'fecha_nacimiento',
                     'email']

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.nombres, obj.apellidos)).upper()
    upper_case_name.short_description = 'Cliente'


class ReservaAdmin(admin.ModelAdmin):

    form = ReservaForm

    class Media:
        js = [
            'clientes/js/reserva.js'
        ]

    readonly_fields = ('estado', 'usuario_registro', 'fecha_hora_registro_reserva',)

    raw_id_fields = ['cliente']

    filter_horizontal = ['mesas']

    fieldsets = [
        ('Descripcion de la Reserva', {'fields': ['descripcion']}),
        ('Cliente', {'fields': ['cliente', 'cliente_documento_reserva', ('direccion_cliente', 'ciudad_cliente', 'pais_cliente'),
                                'telefonos_cliente', 'email']}),
        ('Datos de la Reserva', {'fields': ['fecha_hora_reserva', 'cantidad_personas', 'mesas', 'pago', 'estado']}),
        ('Otros Datos', {'fields': ['usuario_registro', 'fecha_hora_registro_reserva']}),
    ]

    list_display = ('id', 'set_descripcion_reserva', 'cliente', 'fecha_hora_reserva', 'cantidad_personas',
                    'colorea_estado_reserva', 'pago', 'usuario_registro', 'fecha_hora_registro_reserva')
    list_display_links = ['set_descripcion_reserva']
    list_filter = ['cliente', 'fecha_hora_reserva', 'estado', 'usuario_registro']
    search_fields = ['cliente__nombres', 'cliente__apellidos', 'fecha_hora_reserva', 'estado__reserva_estado',
                     'usuario_registro__usuario__username']

    def colorea_estado_reserva(self, obj):
        # color = 'black'
        if obj.estado.reserva_estado == 'UTI':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_reserva_estado_display()))
        elif obj.estado.reserva_estado == 'CAD':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_reserva_estado_display()))
        elif obj.estado.reserva_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_reserva_estado_display()))
        elif obj.estado.reserva_estado == 'VIG':
            color = 'yellowgreen'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_reserva_estado_display()))
        return obj.estado
    colorea_estado_reserva.short_description = 'Estado Reserva'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        reserva_actual = obj

        if not change:
            reserva_actual.estado = ReservaEstado.objects.get(reserva_estado="VIG")

        # reserva_actual.mesas.save()

        if getattr(obj, 'usuario_registro', None) is None:
            obj.usuario_registro = Empleado.objects.get(usuario_id=request.user)
        super(ReservaAdmin, self).save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super(ReservaAdmin, self).save_related(request, form, formsets, change)

        # import pdb
        # pdb.set_trace()

        reserva_actual = form.instance

        if not change:
            # reserva_actual.estado = ReservaEstado.objects.get(reserva_estado='VIG')
            fin = timezone.make_aware(datetime.datetime.combine(reserva_actual.fecha_hora_reserva.date(), reserva_actual.hora_fin_reservas), timezone.get_default_timezone())
            titulo = ("%s - %s - %s" % ('Reserva de Mesa', reserva_actual.cliente, datetime.datetime.strftime(timezone.localtime(reserva_actual.fecha_hora_reserva), '%d/%m/%Y %H:%M:%S'))).upper()
            descripcion = titulo + (" - Cant. de Personas: %s - Mesas: %s" % (reserva_actual.cantidad_personas, "| ".join([str(m) for m in reserva_actual.mesas.all()])))
            event = Event(start=timezone.localtime(reserva_actual.fecha_hora_reserva),
                          end=fin,
                          creation_date=timezone.localtime(timezone.now()),
                          description=descripcion,
                          end_recurring_period=None,
                          title=titulo,
                          category=EventCategory.objects.get(name='Reserva Vigente'),
                          created_by=request.user,
                          image_id=None,
                          rule_id=None)
            event.save()
            reserva_actual.evento_id = event
            reserva_actual.save()

        # En caso de modificaciones sobre la Reserva tambien se debe modificar el Evento en el Calendario
        elif change:
            fin = timezone.make_aware(datetime.datetime.combine(reserva_actual.fecha_hora_reserva.date(), reserva_actual.hora_fin_reservas), timezone.get_default_timezone())
            titulo = ("%s - %s - %s" % ('Reserva de Mesa', reserva_actual.cliente, datetime.datetime.strftime(timezone.localtime(reserva_actual.fecha_hora_reserva), '%d/%m/%Y %H:%M:%S'))).upper()
            descripcion = titulo + (" - Cant. de Personas: %s - Mesas: %s" % (reserva_actual.cantidad_personas, "| ".join([str(m) for m in reserva_actual.mesas.all()])))

            evento = Event.objects.get(pk=reserva_actual.evento_id.id)
            evento.start = timezone.localtime(reserva_actual.fecha_hora_reserva)
            evento.end = fin
            evento.creation_date = timezone.localtime(timezone.now())
            evento.description = descripcion
            evento.title = titulo
            evento.category = EventCategory.objects.get(name='Reserva Vigente')
            evento.created_by=request.user
            evento.save()

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado.reserva_estado == 'VIG':
            return self.readonly_fields + ('descripcion', 'cliente', 'pago')
        elif obj is not None and obj.estado.reserva_estado in ('CAD', 'UTI', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(ReservaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            reserva_actual = Reserva.objects.get(pk=object_id)
            # extra_context['show_button'] = orden_compra_actual.estado_orden_compra.estado_orden_compra \
            #                                not in ('ENT', 'CAN')

            # if orden_compra_actual.estado_orden_compra.estado_orden_compra == 'PEN':
            #     extra_context['show_save_button'] = True
            #     extra_context['show_continue_button'] = True
            #     extra_context['show_addanother_button'] = True
            #     extra_context['show_cancel_button'] = False
            #     extra_context['show_imprimir_button'] = False
            if reserva_actual.estado.reserva_estado in ('CAD', 'UTI', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True
            elif reserva_actual.estado.reserva_estado == 'VIG':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                # extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            # extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(ReservaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado__reserva_estado='VIG')

        # import pdb
        # pdb.set_trace()

        for reserva in queryset:
            now = timezone.localtime(timezone.now())
            print timezone.localtime(reserva.fecha_hora_reserva), now

            if timezone.localtime(reserva.fecha_hora_reserva) < now:
                estado = ReservaEstado.objects.get(reserva_estado='CAD')
                reserva.estado = estado
                reserva.save()
                evento = Event.objects.get(pk=reserva.evento_id.id)
                evento.category = EventCategory.objects.get(name='Reserva Caducada')
                evento.save()

        return super(ReservaAdmin, self).changelist_view(request, extra_context=extra_context)

    # def has_change_permission(self, request, obj=None):
    #     usuario = Empleado.objects.get(usuario=request.user)
    #     if usuario.usuario.is_superuser is not True or usuario.cargo.cargo in ('MO', 'BM'):
    #         return False
    #     else:
    #         return super(ReservaAdmin, self).has_change_permission(request, obj)

# ======================================================================================================================
# @admin.register(CalendarioReserva)
# class CalendarioReservaAdmin(admin.ModelAdmin):
#     # add_form_template = 'http://localhost:8001/calendar/'
#
#     list_display = []
#     list_filter = []
#     search_fields = []
#
#     # def add_view(self, request, form_url='', extra_context=None):
#     #     return super(CalendarioReservaAdmin, self).add_view(request, form_url, extra_context)
# ======================================================================================================================


# class ClienteDocumentoAdmin(admin.ModelAdmin):
#     list_display = ('cliente', 'tipo_documento', 'numero_documento')
#     list_filter = ['cliente', 'tipo_documento', 'numero_documento']
#     search_fields = ['cliente', 'tipo_documento', 'numero_documento']
#
#
# class ClienteTelefonoAdmin(admin.ModelAdmin):
#     list_display = ('cliente', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'telefono')
#     list_filter = ['cliente', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'telefono']
#     search_fields = ['cliente', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'telefono']


# class MyAdminSite(admin.AdminSite):
#     site_header = 'SIGB administracion de Clientes'
#
# admin_site = MyAdminSite(name='myadmin')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva, ReservaAdmin)
# admin.site.register(CalendarioReservaAdmin)
# admin.site.register(ClienteDocumento, ClienteDocumentoAdmin)
# admin.site.register(ClienteTelefono, ClienteTelefonoAdmin)