# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0063_auto_20161008_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='numero_factura_venta',
            field=models.OneToOneField(related_name='numero_factura_venta', verbose_name=b'Numero de Factura', to='bar.NumeroFacturaVenta', help_text=b'El Numero de Factura se asigna al momento de confirmarse la Venta.'),
        ),
    ]
