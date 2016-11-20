# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0073_venta_cliente_documento_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cliente_documento_factura',
            field=models.CharField(help_text=b'Seleccione el Documento del Cliente el cual se registrara en la factura.', max_length=50, null=True, verbose_name=b'Documento', blank=True),
        ),
    ]
