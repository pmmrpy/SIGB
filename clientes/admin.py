from django.contrib import admin

# Register your models here.
from .forms import ClienteForm, ReservaForm  # ClienteDocumentoForm
from .models import Cliente, ClienteTelefono, Reserva, ClienteDocumento  # TelefonoMovilCliente,
# from ajax_select import make_ajax_form
from personal.models import Empleado


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
    verbose_name = 'Telefono del Cliente'
    verbose_name_plural = 'Telefonos del Cliente'


class ClienteAdmin(admin.ModelAdmin):

    class Media:
        js = [
            'clientes/js/rango.js'
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

    list_display = ['id', 'upper_case_name', 'direccion', 'pais', 'ciudad', 'fecha_nacimiento', 'email']  # 'nombres', 'apellidos',
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

    fieldsets = [
        ('Descripcion de la Reserva', {'fields': ['descripcion']}),
        ('Cliente', {'fields': ['cliente']}),
        ('Datos de la Reserva', {'fields': ['fecha_hora_reserva', 'cantidad_personas', 'mesas', 'pago', 'estado']}),
        ('Otros Datos', {'fields': ['usuario_registro', 'fecha_hora_registro_reserva']}),
    ]

    list_display = ('id', 'descripcion', 'cliente', 'fecha_hora_reserva', 'cantidad_personas', 'estado', 'pago',
                    'usuario_registro', 'fecha_hora_registro_reserva')
    list_display_links = ['descripcion']
    list_filter = ['cliente', 'fecha_hora_reserva', 'estado', 'usuario_registro']
    search_fields = ['cliente', 'fecha_hora_reserva', 'estado', 'usuario_registro']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_registro', None) is None:
            obj.usuario_registro = Empleado.objects.get(usuario_id=request.user)
        super(ReservaAdmin, self).save_model(request, obj, form, change)

        # 2) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
        # if obj.


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