# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0148_auto_20160705_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cajaestado',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='cajaestado',
            name='caja_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Caja. (Hasta 3 caracteres', max_length=2, verbose_name=b'Estado de la Caja', choices=[(b'AB', b'Abierta'), (b'CE', b'Cerrada'), (b'CL', b'Clausurada')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 4, 16, 38, 831000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
    ]
