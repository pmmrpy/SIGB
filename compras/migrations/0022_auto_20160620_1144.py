# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0104_auto_20160620_1144'),
        ('compras', '0021_auto_20160619_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='persona_proveedor',
            field=models.ForeignKey(default=1, verbose_name=b'Tipo de Persona', to='bar.Persona', help_text=b'Indique si la Persona es Fisica o Juridica.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 630000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 630000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 626000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 21, 15, 44, 48, 628000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 628000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='unidad_medida_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Unidad de Medida del Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='digito_verificador',
            field=models.IntegerField(default=1, help_text=b'Digito verificador del RUC del Proveedor. Este campo se calcula tomando el RUC ingresado.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 625000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
    ]
