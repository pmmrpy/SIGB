# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0202_auto_20160926_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tiempo_elaboracion',
            field=models.TimeField(help_text=b'Corresponde al tiempo estimado que tomara elaborar el Producto Compuesto', null=True, verbose_name=b'Tiempo Elaboracion', blank=True),
        ),
    ]
