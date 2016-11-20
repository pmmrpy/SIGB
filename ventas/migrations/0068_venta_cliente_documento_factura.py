# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0067_auto_20161013_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente_documento_factura',
            field=models.CharField(default=1, help_text=b'Seleccione el Documento del Cliente el cual se registrara en la factura.', max_length=50, verbose_name=b'Documento'),
        ),
    ]
