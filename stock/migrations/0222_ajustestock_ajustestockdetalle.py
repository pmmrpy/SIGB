# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0415_auto_20161120_1250'),
        ('personal', '0315_auto_20161120_1250'),
        ('stock', '0221_auto_20161120_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjusteStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_registro_ajuste', models.DateTimeField(help_text=b'La fecha y hora de registro del Ajuste de Inventario se asignan al momento de guardar los datos de la misma. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora registro Ajuste de Inventario', auto_now=True)),
                ('motivo_cancelacion', models.CharField(max_length=200, null=True, blank=True)),
                ('observaciones_cancelacion', models.CharField(max_length=200, null=True, blank=True)),
                ('fecha_hora_cancelacion', models.DateTimeField(null=True, blank=True)),
                ('deposito', models.ForeignKey(to='bar.Deposito')),
                ('estado_ajuste', models.ForeignKey(verbose_name=b'Estado Ajuste', to='bar.AjusteStockEstado', help_text=b'El estado del Ajuste de Inventario se asigna de forma automatica.')),
                ('usuario_cancelacion', models.ForeignKey(related_name='usuario_cancelacion_ajuste', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo el Ajuste de Inventario.', null=True, verbose_name=b'Cancelado por?')),
                ('usuario_registra_ajuste', models.ForeignKey(related_name='usuario_registra_ajuste', verbose_name=b'Usuario Realiza Ajuste', to_field=b'usuario', to='personal.Empleado', help_text=b'El usuario logueado que realice el Ajuste de Inventario sera registrado automaticamente en este campo.')),
            ],
            options={
                'verbose_name': 'Ajuste de Inventario',
                'verbose_name_plural': 'Stock - Ajustes de Inventario',
            },
        ),
        migrations.CreateModel(
            name='AjusteStockDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_existente_producto', models.DecimalField(help_text=b'Corresponde a la cantidad existente del Producto en el Deposito seleccionado.', verbose_name=b'Cantidad Existente', max_digits=10, decimal_places=3)),
                ('ajustar', models.BooleanField(default=False, help_text=b'Marque esta casilla si desea ajustar la cantidad existente del Producto en el Deposito seleccionado.', verbose_name=b'Ajustar?')),
                ('cantidad_ajustar_producto', models.DecimalField(help_text=b'Ingrese la cantidad a ajustar del Producto. Debe ingresar la cantidad del Producto que finalmente quedara registrada en el Inventario.', verbose_name=b'Cantidad Ajuste', max_digits=10, decimal_places=3)),
                ('motivo_ajuste', models.CharField(help_text=b'Ingrese el motivo por el cual se realiza el Ajuste de Inventario del Producto seleccionado.', max_length=100, verbose_name=b'Motivo del Ajuste')),
                ('ajuste_stock', models.ForeignKey(to='stock.AjusteStock')),
                ('producto_ajuste', models.ForeignKey(related_name='producto_ajuste_stock', verbose_name=b'Producto a ajustar', to='stock.ProductoExistente', help_text=b'Seleccione el Producto para el cual se realizara el Ajuste de Inventario.')),
                ('unidad_medida', models.ForeignKey(related_name='un_med_ajuste_stock', verbose_name=b'Unidad de Medida', to='bar.UnidadMedidaProducto', help_text=b'Corresponde a la Unidad de Medida de Compra si el Producto es para la Venta o a la Unidad de Medida del Contenido si el Producto es un Insumo.')),
            ],
            options={
                'verbose_name': 'Detalle de Ajuste de Inventario',
                'verbose_name_plural': 'Detalles de Ajustes de Inventario',
            },
        ),
    ]
