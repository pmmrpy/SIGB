# from django import forms
from django.contrib import admin

# Register your models here.
from clientes.forms import ClienteForm, ReservaForm  # ClienteDocumentoForm
from .models import Cliente, ClienteTelefono, Reserva, ClienteDocumento  # TelefonoMovilCliente,


class ClienteDocumentoInline(admin.TabularInline):
    model = ClienteDocumento
    extra = 0
#    form = ClienteDocumentoForm
    min_num = 1
    verbose_name = 'Documento del Cliente'
    verbose_name_plural = 'Documentos del Cliente'


class ClienteTelefonoInline(admin.TabularInline):
    model = ClienteTelefono
    extra = 0
    min_num = 1
    verbose_name = 'Telefono del Cliente'
    verbose_name_plural = 'Telefonos del Cliente'


# class TelefonoMovilClienteInline(admin.TabularInline):
#     model = TelefonoMovilCliente
#     extra = 1


class ClienteAdmin(admin.ModelAdmin):

    form = ClienteForm

    fieldsets = [
        ('Nombres y Apellidos', {'fields': ['nombres', 'apellidos']}),
        ('Informacion Personal', {'fields': ['fecha_nacimiento', 'sexo', 'direccion', ('pais', 'ciudad'), 'email']}),
        # ('Sexo', {'fields': ['sexo']}),
        # ('Direccion / Pais / Ciudad', {'fields': ['direccion', ('pais', 'ciudad')]}),
        # ('Telefonos', {'fields': ['telefono', 'telefono_movil']}),
        # ('Email', {'fields': ['email']}),  # , 'classes': ['collapse']
    ]
    inlines = [ClienteTelefonoInline, ClienteDocumentoInline]

    list_display = ['id', 'nombres', 'apellidos', 'direccion', 'pais', 'ciudad', 'email']
    list_filter = ['nombres', 'apellidos', 'pais', 'ciudad', 'email']
    search_fields = ['id', 'nombres', 'apellidos', 'direccion', 'pais', 'ciudad', 'email']
    

class ReservaAdmin(admin.ModelAdmin):

    form = ReservaForm

    list_display = ('id', 'descripcion', 'cliente', 'fecha_hora', 'estado')
    list_filter = ['cliente', 'fecha_hora', 'estado']
    search_fields = ['cliente', 'fecha_hora', 'estado']


class ClienteDocumentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo_documento', 'numero_documento')
    list_filter = ['cliente', 'tipo_documento', 'numero_documento']
    search_fields = ['cliente', 'tipo_documento', 'numero_documento']


class ClienteTelefonoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono')
    list_filter = ['cliente', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono']
    search_fields = ['cliente', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono']


# class MyAdminSite(admin.AdminSite):
#     site_header = 'SIGB administracion de Clientes'
#
# admin_site = MyAdminSite(name='myadmin')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(ClienteDocumento, ClienteDocumentoAdmin)
admin.site.register(ClienteTelefono, ClienteTelefonoAdmin)