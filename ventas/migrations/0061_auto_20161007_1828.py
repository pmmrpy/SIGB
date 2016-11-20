# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0060_auto_20161007_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='forma_pago',
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_apertura_caja',
            field=models.DateTimeField(help_text=b'Fecha en la que se realiza la Apertura de Caja.', verbose_name=b'Fecha Apertura', auto_now_add=True),
        ),
    ]
