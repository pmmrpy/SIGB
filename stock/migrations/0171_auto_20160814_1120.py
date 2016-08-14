# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0170_auto_20160812_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productocompuesto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='productocompuesto',
            name='subcategoria',
        ),
        migrations.RemoveField(
            model_name='productocompuesto',
            name='tipo_producto',
        ),
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='compuesto',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ProductoCompuesto',
        ),
        migrations.CreateModel(
            name='ProductoCompuesto',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('stock.producto',),
        ),
    ]
