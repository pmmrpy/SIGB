# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0286_auto_20161111_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='descripcion',
            field=models.CharField(default=b'Reserva de Mesa', help_text=b'Puede ingresar alguna descripcion que identifique a la Reserva.', max_length=300, verbose_name=b'Descripcion Reserva'),
        ),
    ]
