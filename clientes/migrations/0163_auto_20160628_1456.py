# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0138_auto_20160628_1456'),
        ('clientes', '0162_auto_20160628_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientetelefono',
            name='codigo_ciudad_operadora_telefono',
        ),
        migrations.AddField(
            model_name='clientetelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(default=1, verbose_name=b'Codigo de Ciudad/Operadora - Telefono', to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 310000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 313000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.'),
        ),
    ]
