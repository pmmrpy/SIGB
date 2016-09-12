# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0173_auto_20160830_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado Compra', to='bar.CompraEstado', help_text=b'La Compra puede tener 3 estados: PENDIENTE, CONFIRMADA o CANCELADA. El estado se asigna de forma automatica de acuerdo a la accion realizada.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora Compra', auto_now=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date.today, help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha Factura Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.DecimalField(default=1, help_text=b'Ingrese el Numero de Factura que acompana la Compra.', verbose_name=b'Numero de Factura Compra', max_digits=7, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_orden_compra',
            field=models.OneToOneField(verbose_name=b'Numero Orden de Compra', to='compras.OrdenCompra', help_text=b'Seleccione el Numero de Orden de Compra para la cual se confirmara la Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total_compra',
            field=models.DecimalField(default=0, help_text=b'Este campo se calcula en funcion al detalle de la Compra.', verbose_name=b'Total Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=django.utils.timezone.now, help_text=b'Registra la fecha del movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='monto_movimiento',
            field=models.DecimalField(default=0, help_text=b'Registra el Monto del Movimiento.', verbose_name=b'Monto del Movimiento', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='numero_comprobante',
            field=models.IntegerField(help_text=b'Corresponde al Numero de Factura o Numero de Comprobante de Pago del movimiento.', verbose_name=b'Numero Comprobante Movimiento'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='tipo_movimiento',
            field=models.CharField(help_text=b'Registra el Tipo de Movimiento.', max_length=3, verbose_name=b'Tipo de Movimiento', choices=[(b'PAG', b'Pago'), (b'FAC', b'Factura')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 1, 16, 42, 44, 584000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
    ]
