# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0077_auto_20161016_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='venta_ocasional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='usuario_solicitante',
            field=models.ForeignKey(related_name='usuario_solicitante_comanda', verbose_name=b'Solicitado por?', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.'),
        ),
    ]
