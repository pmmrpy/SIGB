# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0036_auto_20160815_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.OneToOneField(verbose_name=b'Numero de Pedido', to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.'),
        ),
    ]
