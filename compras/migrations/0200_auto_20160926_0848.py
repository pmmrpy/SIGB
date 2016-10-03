# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0272_auto_20160827_2010'),
        ('compras', '0199_auto_20160925_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='usuario_modifica_orden_compra',
            field=models.ForeignKey(related_name='usuario_modifica', default=17, verbose_name=b'Modificado por?', to='personal.Empleado', help_text=b'Usuario que modifico la Orden de Compra.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora Compra', auto_now=True),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='unidad_medida_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Un. Med. Compra Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 27, 12, 48, 19, 252000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='numero_orden_compra',
            field=models.AutoField(help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', serialize=False, verbose_name=b'Nro. Ord. Compra', primary_key=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total Ord. Compra', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='cantidad_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a adquirir del producto.', verbose_name=b'Cantidad Producto', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='precio_producto_orden_compra',
            field=models.DecimalField(help_text=b'Ingrese el precio de compra del producto definido por el proveedor.', verbose_name=b'Precio Compra Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='total_producto_orden_compra',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='unidad_medida_orden_compra',
            field=models.ForeignKey(verbose_name=b'Un. Med. Compra Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
    ]
