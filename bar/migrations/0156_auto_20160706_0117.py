# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0155_auto_20160706_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajaestado',
            name='caja_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Caja. (Hasta 2 caracteres', max_length=2, verbose_name=b'Estado de la Caja', choices=[(b'AB', b'Abierta'), (b'CE', b'Cerrada'), (b'CL', b'Clausurada')]),
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='codigo_operadora_telefono',
            field=models.PositiveIntegerField(help_text=b'Codigo de la Operadora de Telefonia.', verbose_name=b'Codigo Telefonico de la Operadora'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 5, 17, 36, 795000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='codigo_moneda',
            field=models.PositiveIntegerField(help_text=b'Corresponde al codigo internacional ISO 4217 de la Moneda. EJ: Gs - 600', unique=True, verbose_name=b'Codigo de Moneda ISO 4217'),
        ),
    ]
