# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0076_auto_20161016_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='cantidad_solicitada',
            field=models.DecimalField(default=1, verbose_name=b'Cantidad Solicitada', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='tiempo_estimado_procesamiento',
            field=models.TimeField(help_text=b'Corresponde al tiempo estimado que tomara elaborar el Producto Compuesto', verbose_name=b'Tiempo Estimado Procesamiento'),
        ),
    ]
