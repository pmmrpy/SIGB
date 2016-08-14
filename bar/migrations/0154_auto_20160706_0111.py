# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0153_auto_20160706_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservaestado',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='codigo_operadora_telefono',
            field=models.IntegerField(help_text=b'Codigo de la Operadora de Telefonia.', verbose_name=b'Codigo Telefonico de la Operadora'),
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo Telefonico del Pais', to='bar.CodigoPaisTelefono'),
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='tipo_operadora',
            field=models.CharField(help_text=b'Tipo de Telefonia', max_length=2, verbose_name=b'Tipo de Operadora de Telefonia', choices=[(b'TM', b'Telefonia Movil'), (b'TF', b'Telefonia Fija')]),
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='codigo_pais_telefono',
            field=models.PositiveIntegerField(help_text=b'Codigo internacional del pais al cual corresponde el telefono.', unique=True, verbose_name=b'Codigo Telefonico del Pais'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 5, 11, 47, 592000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='moneda',
            field=models.CharField(help_text=b'Nombre de la Moneda.', unique=True, max_length=100, verbose_name=b'Moneda'),
        ),
        migrations.AlterField(
            model_name='reservaestado',
            name='reserva_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Reserva. (Hasta 1 caracter)', max_length=1, verbose_name=b'Estado de la Reserva', choices=[(b'VI', b'Vigente'), (b'CA', b'Caducada'), (b'UT', b'Utilizada')]),
        ),
    ]
