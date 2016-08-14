# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0067_auto_20151215_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientedocumento',
            options={'verbose_name': 'Cliente - Documento', 'verbose_name_plural': 'Clientes - Documentos'},
        ),
        migrations.AlterModelOptions(
            name='clientetelefono',
            options={'verbose_name': 'Cliente - Telefono', 'verbose_name_plural': 'Clientes - Telefonos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 90000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 92000, tzinfo=utc)),
        ),
    ]
