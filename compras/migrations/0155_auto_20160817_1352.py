# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0154_auto_20160817_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='actividad_economica',
            field=models.CharField(default=b'Compra/venta de productos gastronomicos', help_text=b'Ingrese la actividad economica a la que se dedica la Empresa.', max_length=100, verbose_name=b'Actividad Economica'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='codigo_establecimiento',
            field=models.CharField(default=b'001', help_text=b'Ingrese el Codigo de Establecimiento.', max_length=3, verbose_name=b'Codigo de Establecimiento'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_factura_compra',
            field=models.IntegerField(default=1, help_text=b'Ingrese el Numero de Factura que acompana la Compra.', max_length=7, verbose_name=b'Numero de Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 17, 52, 49, 412000, tzinfo=utc), help_text=b'Ingrese la fecha del Movimiento.', verbose_name=b'Fecha Registro Movimiento'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 17, 52, 49, 417000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='fecha_pago_proveedor',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 17, 52, 49, 413000, tzinfo=utc), help_text=b'Ingrese la fecha del Pago al Proveedor.', verbose_name=b'Fecha Pago Proveedor'),
        ),
    ]
