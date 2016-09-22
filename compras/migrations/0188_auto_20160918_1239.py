# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0272_auto_20160827_2010'),
        ('compras', '0187_auto_20160911_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenPago',
            fields=[
                ('numero_orden_pago', models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Pago.', serialize=False, verbose_name=b'Numero Orden de Pago', primary_key=True)),
                ('fecha_hora_orden_pago', models.DateTimeField(help_text=b'La fecha y hora de la Orden de Pago se asignan al momento de guardar los datos del pago. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Orden de Pago', auto_now_add=True)),
                ('total_orden_pago', models.DecimalField(default=0, verbose_name=b'Total Orden de Pago', max_digits=18, decimal_places=0)),
                ('proveedor_orden_pago', models.ForeignKey(to='compras.Proveedor')),
                ('usuario_registro_orden_pago', models.ForeignKey(related_name='usuario_registro_orden_pago', verbose_name=b'Preparado por?', to='personal.Empleado', help_text=b'Usuario que registro la Orden de Pago.')),
            ],
            options={
                'verbose_name': 'Orden de Pago Proveedor',
                'verbose_name_plural': 'Proveedores - Ordenes de Pago',
            },
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.CharField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', max_length=15, verbose_name=b'Numero de Factura Compra', blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.OneToOneField(blank=True, to='compras.OrdenCompra', help_text=b'Numero Orden de Compra seleccionada.', verbose_name=b'Numero Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 19, 16, 39, 31, 561000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        # migrations.AddField(
        #     model_name='facturaproveedor',
        #     name='numero_orden_pago',
        #     field=models.OneToOneField(to='compras.OrdenPago'),
        # ),
    ]
