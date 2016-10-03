# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0041_auto_20160926_1600'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CierreCaja',
        ),
        migrations.DeleteModel(
            name='MovimientoCaja',
        ),
    ]
