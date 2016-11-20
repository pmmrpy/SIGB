# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0280_auto_20161025_2131'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalendarioReserva',
        ),
    ]
