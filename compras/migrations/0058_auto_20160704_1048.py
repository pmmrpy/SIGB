# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0057_auto_20160628_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado_compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='numero_orden_compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='compradetalle',
            name='producto_compra',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='proveedor_ptr',
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 361000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 14, 48, 34, 364000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 364000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 360000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='proveedortelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(help_text=b'Seleccione o ingrese el codigo de ciudad u operadora de telefonia movil.', to='bar.CodigoOperadoraTelefono'),
        ),
        migrations.AlterField(
            model_name='proveedortelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(to='bar.CodigoPaisTelefono'),
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='CompraDetalle',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
