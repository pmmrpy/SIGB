# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0048_auto_20160928_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='area_encargada',
            field=models.CharField(max_length=3, verbose_name=b'Area Encargada', choices=[(b'COC', b'Cocina'), (b'BAR', b'Barra')]),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='estado_comanda',
            field=models.CharField(max_length=3, verbose_name=b'Estado Comanda', choices=[(b'PEN', b'Pendiente'), (b'PRO', b'Procesada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='fecha_hora_pedido_comanda',
            field=models.DateTimeField(verbose_name=b'Fecha/hora Pedido Comanda'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='fecha_hora_procesamiento_comanda',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha/hora Procesamiento Comanda', blank=True),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='producto_a_elaborar',
            field=models.ForeignKey(verbose_name=b'Producto a Elaborar', to='stock.ProductoCompuesto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='apertura_caja',
            field=models.ForeignKey(default=1, verbose_name=b'Apertura de Caja', to='ventas.AperturaCaja', help_text=b'Se asigna dependiendo del usuario logueado y de si posee una Apertura de Caja vigente.'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.ForeignKey(related_name='numero_factura', default=1, verbose_name=b'Numero de Factura de la Venta', to='bar.FacturaVenta', help_text=b'El Numero de Factura se asigna al momento de confirmarse la Venta.'),
        ),
    ]
