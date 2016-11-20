# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0285_reserva_evento_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='evento_id',
            field=models.ForeignKey(blank=True, to='calendarium.Event', null=True),
        ),
    ]
