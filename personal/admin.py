from django.contrib import admin
# from django.db import models

# Register your models here.
from personal.forms import EmpleadoForm, EmpleadoTelefonoForm
from .models import Empleado, EmpleadoTelefono, Cargo, Horario, EmpleadoDocumento
# from .widgets import RichTextEditorWidget
from random import randint


class EmpleadoDocumentoInline(admin.TabularInline):
    model = EmpleadoDocumento
    extra = 0
    readonly_fields = ['digito_verificador']
    min_num = 1
    verbose_name = 'Documento del Empleado'
    verbose_name_plural = 'Documentos del Empleado'


class EmpleadoTelefonoInline(admin.TabularInline):
    model = EmpleadoTelefono
    form = EmpleadoTelefonoForm
    extra = 0
    min_num = 1
    verbose_name = 'Telefono del Empleado'
    verbose_name_plural = 'Telefonos del Empleado'


class EmpleadoAdmin(admin.ModelAdmin):

    class Media:
        js = [
            'personal/js/empleado.js'
        ]

    form = EmpleadoForm

    readonly_fields = ['_codigo_venta']

    fieldsets = [
        ('Nombres y Apellidos', {'fields': ['nombres', 'apellidos']}),
        ('Informacion Personal', {'fields': ['fecha_nacimiento', 'sexo', 'direccion', 'pais', 'ciudad', 'barrio',
                                             'email']}),
        # ('Sexo', {'fields': ['sexo']}),
        # ('Direccion', {'fields': ['direccion']}),
        ('Datos Laborales', {'fields': ['cargo', 'sector', 'salario', 'horario', 'usuario', '_codigo_venta']}),
        # ('Email', {'fields': ['email']}),  # , 'classes': ['collapse']
    ]

    inlines = [EmpleadoTelefonoInline, EmpleadoDocumentoInline]

    list_display = ['id', 'upper_case_name', 'fecha_nacimiento', 'direccion', 'pais', 'ciudad', 'barrio',
                    'cargo', 'sector', 'horario', 'usuario', 'email']  # 'nombres', 'apellidos',
    list_display_links = ['upper_case_name']
    list_filter = ['id', 'nombres', 'apellidos', 'direccion', 'cargo', 'sector', 'horario', 'usuario', 'email']
    search_fields = ['id', 'nombres', 'apellidos', 'direccion', 'cargo__cargo', 'sector__sector', 'horario__horario',
                     'usuario__username', 'email']

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.nombres, obj.apellidos)).upper()
    upper_case_name.short_description = 'Empleado'

    def save_model(self, request, obj, form, change):
        if obj._codigo_venta is None:
            obj._codigo_venta = randint(100, 999)
        super(EmpleadoAdmin, self).save_model(request, obj, form, change)

# class EmpleadoDocumentoAdmin(admin.ModelAdmin):
#     list_display = ['empleado', 'tipo_documento', 'numero_documento']
#     list_filter = ['empleado', 'tipo_documento', 'numero_documento']
#     search_fields = ['empleado', 'tipo_documento', 'numero_documento']


class HorarioAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Descripcion', {'fields': ['horario']}),
        ('Horario', {'fields': ['horario_inicio', 'horario_fin', 'duracion_jornada']}),
    ]

    ordering = ['id']
    list_display = ['id', 'horario', 'horario_inicio', 'horario_fin', 'duracion_jornada']
    list_display_links = ['horario']
    list_filter = ['id', 'horario', 'horario_inicio', 'horario_fin']
    search_fields = ['id', 'horario', 'horario_inicio', 'horario_fin']


class CargoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cargo']
    list_display_links = ['cargo']
    list_filter = ['id', 'cargo']
    search_fields = ['id', 'cargo']


# class EmpleadoTelefonoAdmin(admin.ModelAdmin):
#
#     # form = EmpleadoTelefonoForm
#
#     list_display = ['empleado', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono']
#     list_filter = ['empleado', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono']
#     search_fields = ['empleado', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'telefono']

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Horario, HorarioAdmin)
# admin.site.register(EmpleadoDocumento, EmpleadoDocumentoAdmin)
admin.site.register(Cargo, CargoAdmin)
# admin.site.register(EmpleadoTelefono, EmpleadoTelefonoAdmin)