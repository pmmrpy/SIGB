# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0276_auto_20160827_2010'),
        ('ventas', '0070_remove_venta_cliente_documento_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente_documento_factura',
            field=models.ForeignKey(blank=True, to='clientes.ClienteDocumento', help_text=b'Seleccione el Documento del Cliente el cual se registrara en la factura.', null=True, verbose_name=b'Documento'),
        ),
    ]
