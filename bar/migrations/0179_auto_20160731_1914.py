# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0096_auto_20160731_1914'),
        ('ventas', '0021_auto_20160731_1914'),
        ('bar', '0178_auto_20160731_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='proveedor_ptr',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 23, 14, 5, 846000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='empresa',
            field=models.ForeignKey(default=1, to='compras.Empresa'),
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
