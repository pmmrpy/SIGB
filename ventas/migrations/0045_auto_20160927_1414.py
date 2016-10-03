# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0044_aperturacaja_cierrecaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='apertura_caja',
            field=models.ForeignKey(default=1, to='ventas.AperturaCaja'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_apertura_caja',
            field=models.DateField(help_text=b'Fecha en la que se realiza la Apertura de Caja.', auto_now_add=True),
        ),
    ]
