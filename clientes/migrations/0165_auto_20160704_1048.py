# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0164_auto_20160628_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 349000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo de Operadora - Telefono', to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione el codigo de operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo de Pais - Telefono', to='bar.CodigoPaisTelefono', help_text=b'Seleccione el codigo de pais para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 353000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.'),
        ),
    ]
