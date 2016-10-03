# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0055_auto_20161002_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='anulado',
        ),
    ]
