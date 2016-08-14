# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0025_auto_20160620_1304'),
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
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='estado_linea_credito_proveedor',
            field=models.BooleanField(help_text=b'Solo una Linea de Credito puede estar activa.La intencion es llevar un control de los cambios de la Linea de Credito en el tiempo.', verbose_name=b'Activo?'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 161000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='linea_credito_proveedor',
            field=models.IntegerField(help_text=b'Ingrese el monto ofrecido por el proveedor como Linea de Credito.', verbose_name=b'Monto'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 14, 4, 163000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 163000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='proveedor_orden_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Proveedor', to='compras.Proveedor', help_text=b'Seleccione el Proveedor al cual se le realizara la Orden de Compra.'),
        ),
        migrations.RemoveField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
        ),
        migrations.AddField(
            model_name='ordencompradetalle',
            name='producto_orden_compra',
            field=models.ManyToManyField(help_text=b'Seleccione un Producto a ordenar.', related_name='orden_compra_productos', verbose_name=b'Producto', to='compras.ProductoProveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 14, 4, 160000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='persona_proveedor',
            field=models.ForeignKey(default=1, verbose_name=b'Persona', to='bar.Persona', help_text=b'Indique si el Proveedor tiene personeria Fisica o Juridica.'),
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='CompraDetalle',
        ),
    ]
