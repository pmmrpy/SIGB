# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0274_auto_20160918_2134'),
        ('compras', '0190_auto_20160918_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenPagoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura_compra', models.IntegerField(help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra')),
                ('fecha_factura_compra', models.DateField(default=datetime.date.today, help_text=b'Ingrese la fecha de la Factura.', verbose_name=b'Fecha de la Factura Compra')),
                ('plazo_factura_compra', models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en dias para el pago.', verbose_name=b'Plazo de Pago Compra')),
                ('total_factura_compra', models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente en funcion al detalle de la Compra.', verbose_name=b'Monto Total de la Factura Compra', max_digits=18, decimal_places=0)),
                ('estado_factura_compra', models.CharField(blank=True, help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura Compra', choices=[(b'EPP', b'En Plazo de Pago'), (b'FPP', b'Fuera del Plazo de Pago'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')])),
                ('procesado', models.BooleanField(default=False, help_text=b'Marque esta casilla si la factura sera incluida en la Orden de Pago.', verbose_name=b'Procesar?')),
                ('compra', models.ForeignKey(verbose_name=b'Compra Asociada', to='compras.Compra', help_text=b'Seleccione la Compra cuya Factura sera registrada.')),
                ('forma_pago_compra', models.ForeignKey(verbose_name=b'Forma de Pago Compra', to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta Factura.')),
            ],
            options={
                'verbose_name': 'Detalle Orden de Pago Proveedor',
                'verbose_name_plural': 'Ordenes de Pago Proveedores - Detalles',
            },
        ),
        migrations.RemoveField(
            model_name='facturaproveedor',
            name='numero_orden_pago',
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='estado_orden_pago',
            field=models.CharField(blank=True, help_text=b'Se asigna automaticamente de acuerdo a la accion que se realicecon la Orden de Pago.', max_length=3, verbose_name=b'Estado Orden de Pago', choices=[(b'PEN', b'Pendiente'), (b'CON', b'Confirmada'), (b'ANU', b'Anulada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 20, 1, 34, 19, 658000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AddField(
            model_name='ordenpagodetalle',
            name='numero_orden_pago',
            field=models.ForeignKey(to='compras.OrdenPago'),
        ),
        migrations.AddField(
            model_name='ordenpagodetalle',
            name='proveedor',
            field=models.ForeignKey(verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor.'),
        ),
        migrations.AddField(
            model_name='ordenpagodetalle',
            name='tipo_factura_compra',
            field=models.ForeignKey(verbose_name=b'Tipo de Factura Compra', to='bar.TipoFacturaCompra', help_text=b'Seleccione el Tipo de Factura.'),
        ),
    ]
