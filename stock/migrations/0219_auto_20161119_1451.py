# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0218_auto_20161119_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoExistente',
            fields=[
            ],
            options={
                'verbose_name': 'Producto Existente',
                'proxy': True,
                'verbose_name_plural': 'Productos - Productos Existentes',
            },
            bases=('stock.producto',),
        ),
        migrations.AlterField(
            model_name='transferenciastockdetalle',
            name='producto_transferencia',
            field=models.ForeignKey(related_name='producto_solicitado', verbose_name=b'Producto a transferir', to='stock.ProductoExistente', help_text=b'Seleccione el producto a transferir entre Depositos.'),
        ),
    ]
