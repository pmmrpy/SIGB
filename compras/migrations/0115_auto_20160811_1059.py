# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0114_auto_20160810_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaCreditoProveedorDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_movimiento', models.DecimalField(default=0, help_text=b'Ingrese el Monto del Movimiento.', verbose_name=b'Monto del Movimiento', max_digits=18, decimal_places=0)),
                ('tipo_movimiento', models.CharField(help_text=b'Seleccione el Tipo de Movimiento.', max_length=3, verbose_name=b'Tipo de Movimiento', choices=[(b'PAG', b'Pago'), (b'FAC', b'Factura')])),
                ('numero_comprobante', models.IntegerField(help_text=b'Ingrese el Numero de Comprobante del Movimiento.', verbose_name=b'Numero Comprobante Movimiento')),
                ('fecha_movimiento', models.DateField(default=datetime.datetime(2016, 8, 11, 14, 59, 18, 634000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento')),
            ],
            options={
                'verbose_name': 'Linea de Credito con Proveedor - Detalle',
                'verbose_name_plural': 'Lineas de Credito con Proveedores - Detalles',
            },
        ),
        migrations.AlterModelOptions(
            name='facturaproveedor',
            options={'verbose_name': 'Proveedor - Factura/Pago', 'verbose_name_plural': 'Proveedores - Facturas/Pagos'},
        ),
        migrations.AddField(
            model_name='facturaproveedor',
            name='total_factura_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion al detalle de la Compra.', verbose_name=b'Monto Total de la Factura', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='monto_total_facturas_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente y corresponde a la suma de todas las Facturas registradas para el Proveedor.', verbose_name=b'Monto Total Facturas', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='monto_total_pagos_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente y corresponde a la suma de todos los Pagos registrados para el Proveedor.', verbose_name=b'Monto Total Pagos', max_digits=18, decimal_places=0),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='uso_linea_credito_proveedor',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente como la diferencia entre el Monto Total de las Facturas contra el Monto Total de los Pagos.', verbose_name=b'Monto Utilizado Linea de Credito', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 11), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 11), help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='total_pago_factura',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion a los pagos registrados para la Factura.', verbose_name=b'Total Pagado de la Factura', max_digits=18, decimal_places=0),
        ),
        # migrations.AlterField(
        #     model_name='lineacreditoproveedor',
        #     name='estado_linea_credito_proveedor',
        #     field=models.CharField(default=b'DEL', help_text=b'Se asigna automaticamente de acuerdo a la utilizacion de la Linea de Credito.', max_length=3, verbose_name=b'Estado Linea de Credito', choices=[(b'DEL', b'Dentro de la Linea de Credito'), (b'SOB', b'Sobregirada')]),
        # ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro', auto_now=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 12, 14, 59, 18, 639000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 14, 59, 18, 639000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 11, 14, 59, 18, 636000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='numero_comprobante_pago',
            field=models.IntegerField(default=0, help_text=b'Ingrese el Numero del Comprobante de Pago.', verbose_name=b'Numero de Comprobante de Pago'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='numero_nota_credito',
            field=models.IntegerField(default=0, help_text=b'Ingrese el Numero de la Nota de Credito que anula o cancela la factura de la Compra en caso de que la misma se haya devuelto o cancelado.', verbose_name=b'Numero Nota de Credito'),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedordetalle',
            name='linea_credito_proveedor',
            field=models.ForeignKey(to='compras.LineaCreditoProveedor'),
        ),
    ]
