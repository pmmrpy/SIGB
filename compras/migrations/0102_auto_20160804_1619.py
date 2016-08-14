# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0101_auto_20160803_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_pago_proveedor', models.DecimalField(default=0, help_text=b'Ingrese el monto abonado al Proveedor.', verbose_name=b'Monto de Pago al Proveedor', max_digits=18, decimal_places=0)),
                ('fecha_pago_proveedor', models.DateTimeField(help_text=b'La fecha y hora del Pago al Proveedor se asignan al momento de guardar los datos del Pago. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/Hora Pago Proveedor', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pago a Proveedores',
                'verbose_name_plural': 'Pagos a Proveedores',
            },
        ),
        migrations.AlterModelOptions(
            name='lineacreditoproveedor',
            options={'verbose_name': 'Linea de Credito con Proveedor', 'verbose_name_plural': 'Lineas de Credito con Proveedores'},
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.date(2016, 8, 4), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='linea_credito_proveedor',
            field=models.DecimalField(default=0, help_text=b'Ingrese el monto ofrecido por el proveedor como Linea de Credito.', verbose_name=b'Monto Linea de Credito', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 5, 20, 19, 24, 782000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='compra',
            field=models.ForeignKey(help_text=b'Seleccione la Compra a la cual se aplicara el Pago.', to='compras.Compra'),
        ),
    ]
