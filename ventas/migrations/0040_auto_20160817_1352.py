# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0039_auto_20160815_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.ForeignKey(default=1, verbose_name=b'Numero de Factura de la Venta', to='bar.FacturaVenta', help_text=b''),
        ),
    ]
