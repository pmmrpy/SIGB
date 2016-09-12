import datetime
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from bar.models import ReservaEstado
from .forms import ClienteForm, ReservaForm, ClienteTelefonoForm  # ClienteDocumentoForm
from .models import Cliente, ClienteTelefono, Reserva, ClienteDocumento  # TelefonoMovilCliente,
# from ajax_select import make_ajax_form
from personal.models import Empleado

# Register your models here.


class ClienteDocumentoInline(admin.TabularInline):
    model = ClienteDocumento
    extra = 0
#    form = ClienteDocumentoForm
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

    class Media:
        js = [
            'clientes/js/rango.js',
            'clientes/js/change_form.js'
        ]

    form = ClienteForm

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

    readonly_fields = ('estado', 'usuario_registro', 'fecha_hora_registro_reserva',)

    raw_id_fields = ['cliente']

    filter_horizontal = ['mesas']

    fieldsets = [
        ('Descripcion de la Reserva', {'fields': ['descripcion']}),
        ('Cliente', {'fields': ['cliente']}),
        ('Datos de la Reserva', {'fields': ['fecha_hora_reserva', 'cantidad_personas', 'mesas', 'pago', 'estado']}),
        ('Otros Datos', {'fields': ['usuario_registro', 'fecha_hora_registro_reserva']}),
    ]

    list_display = ('id', 'descripcion_reserva', 'cliente', 'fecha_hora_reserva', 'cantidad_personas',
                    'colorea_estado_reserva', 'pago', 'usuario_registro', 'fecha_hora_registro_reserva')
    list_display_links = ['descripcion_reserva']
    list_filter = ['cliente', 'fecha_hora_reserva', 'estado', 'usuario_registro']
    search_fields = ['cliente__nombres', 'cliente__apellidos', 'fecha_hora_reserva', 'estado__reserva_estado',
                     'usuario_registro__usuario__username']

    def descripcion_reserva(self, obj):
        # fecha_hora_reserva = (obj.fecha_hora_reserva).astimezone(timezone.utc)
        return ("%s - %s - %s" % (obj.descripcion, obj.cliente,
                                  datetime.datetime.strftime(timezone.localtime(obj.fecha_hora_reserva),
                                                             '%d/%m/%Y %H:%M:%S'))).upper()
    descripcion_reserva.short_description = 'Descripcion Reserva'

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
        if getattr(obj, 'usuario_registro', None) is None:
            obj.usuario_registro = Empleado.objects.get(usuario_id=request.user)
        super(ReservaAdmin, self).save_model(request, obj, form, change)

        # 2) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
        # if obj.

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado.reserva_estado in ('CAD', 'UTI', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(ReservaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            reserva_actual = Reserva.objects.get(pk=object_id)
            extra_context['show_button'] = reserva_actual.estado.reserva_estado not in ('CAD', 'UTI', 'CAN')

        return super(ReservaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado__reserva_estado='VIG')

        for reserva in queryset:
            now = timezone.localtime(timezone.now())
            print timezone.localtime(reserva.fecha_hora_reserva), now

            if timezone.localtime(reserva.fecha_hora_reserva) < now:
                estado = ReservaEstado.objects.get(reserva_estado='CAD')
                reserva.estado = estado
                reserva.save()

        return super(ReservaAdmin, self).changelist_view(request, extra_context=extra_context)


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
# admin.site.register(ClienteDocumento, ClienteDocumentoAdmin)
# admin.site.register(ClienteTelefono, ClienteTelefonoAdmin)