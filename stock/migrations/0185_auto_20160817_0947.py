# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0237_auto_20160817_0947'),
        ('stock', '0184_auto_20160816_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdetalle',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='id_movimiento',
            field=models.PositiveIntegerField(default=1, help_text=b'Identificador del movimiento en el Stock.', verbose_name=b'ID Movimiento'),
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='ubicacion_destino',
            field=models.ForeignKey(related_name='ubicacion_destino', default=1, to='bar.Deposito', help_text=b'Ubicacion a donde se dirige el movimiento de Stock.'),
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='ubicacion_origen',
            field=models.ForeignKey(related_name='ubicacion_origen', default=6, to='bar.Deposito', help_text=b'Ubicacion desde donde se origina el movimiento de Stock.'),
        ),
    ]
