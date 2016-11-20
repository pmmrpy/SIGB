# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0228_auto_20161007_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.OneToOneField(blank=True, to='compras.OrdenCompra', help_text=b'Numero Orden de Compra seleccionada.', verbose_name=b'Nro. Orden Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 21, 17, 57, 93000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='estado_orden_pago',
            field=models.ForeignKey(verbose_name=b'Estado Orden Pago', blank=True, to='bar.OrdenPagoEstado', help_text=b'Se asigna automaticamente de acuerdo a la accion que se realice con la Orden de Pago.'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='fecha_hora_orden_pago',
            field=models.DateTimeField(help_text=b'La fecha y hora de la Orden de Pago se asignan al momento de guardar los datos del pago. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Orden Pago', auto_now=True),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='numero_orden_pago',
            field=models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Pago.', serialize=False, verbose_name=b'Numero Orden Pago', primary_key=True),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='total_orden_pago',
            field=models.DecimalField(default=0, verbose_name=b'Total Orden Pago', max_digits=18, decimal_places=0),
        ),
    ]
