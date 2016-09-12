# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0188_auto_20160826_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_elaboracion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_vencimiento',
        ),
    ]
