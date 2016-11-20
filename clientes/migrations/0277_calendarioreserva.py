# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0276_auto_20160827_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarioReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Calendario de Reservas',
                'verbose_name_plural': 'Calendario de Reservas',
            },
        ),
    ]
