# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0151_auto_20160706_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesaestado',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 4, 30, 14, 428000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='mesaestado',
            name='mesa_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Mesa. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Estado de la Mesa', choices=[(b'AC', b'Activa'), (b'IN', b'Inactiva'), (b'OC', b'Ocupada'), (b'DI', b'Disponible')]),
        ),
    ]
