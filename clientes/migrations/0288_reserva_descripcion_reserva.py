# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0287_auto_20161114_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='descripcion_reserva',
            field=models.CharField(default=b'Reserva de Mesa', max_length=300, blank=True, help_text=b'Puede ingresar alguna descripcion que identifique a la Reserva.', null=True, verbose_name=b'Descripcion Reserva'),
        ),
    ]
