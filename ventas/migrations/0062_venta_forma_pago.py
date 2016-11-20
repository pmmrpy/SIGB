# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0314_auto_20161007_1830'),
        ('ventas', '0061_auto_20161007_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='forma_pago',
            field=models.ForeignKey(default=1, verbose_name=b'Forma de Pago', to='bar.FormaPagoVenta', help_text=b'Seleccione la Forma de Pago.'),
        ),
    ]
