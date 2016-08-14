# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0040_auto_20151215_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compradetalle',
            options={'verbose_name': 'Compra - Detalle', 'verbose_name_plural': 'Compras - Detalles'},
        ),
        migrations.AlterModelOptions(
            name='productoproveedor',
            options={'verbose_name': 'Producto por Proveedor', 'verbose_name_plural': 'Productos por Proveedor'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='telefonoproveedor',
            options={'verbose_name': 'Proveedor - Telefono', 'verbose_name_plural': 'Proveedores - Telefonos'},
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(default=b'Ingrese direccion.', help_text=b'Direccion del proveedor. (Hasta 200 caracteres)', max_length=200),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='pagina_web',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 20, 27, 48, 105000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 105000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor',
            field=models.CharField(help_text=b'Nombre del proveedor. (Hasta 100 caracteres)', max_length=100),
        ),
    ]
