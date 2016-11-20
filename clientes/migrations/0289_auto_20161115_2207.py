# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0288_reserva_descripcion_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='descripcion_reserva',
            field=models.CharField(help_text=b'Puede ingresar alguna descripcion que identifique a la Reserva.', max_length=300, null=True, verbose_name=b'Descripcion Reserva', blank=True),
        ),
    ]
