# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_auto_20151025_1138'),
        ('ventas', '0002_pedido_pedidodetalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='ubicacion',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mesa',
            field=models.ForeignKey(to='bar.Mesa'),
        ),
        migrations.DeleteModel(
            name='Caja',
        ),
        migrations.DeleteModel(
            name='CajaUbicacion',
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
        migrations.DeleteModel(
            name='MesaUbicacion',
        ),
    ]
