# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_auto_20151107_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='proveedor',
            new_name='proveedor_compra',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 18, 49, 1, 734000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 18, 49, 1, 734000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='compra',
            field=models.ForeignKey(related_name='compra', to='compras.Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=8, help_text=b'RUC del proveedor.', unique=True, verbose_name=b'RUC'),
        ),
    ]
