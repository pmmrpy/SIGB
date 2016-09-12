# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0034_auto_20160815_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='reserva',
            field=models.ForeignKey(blank=True, to='clientes.Reserva', help_text=b'Seleccione una Reserva en caso de que el Cliente haya realizado una.'),
        ),
    ]
