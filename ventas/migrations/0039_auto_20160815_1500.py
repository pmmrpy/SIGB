# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0038_auto_20160815_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='mozo_pedido',
            field=models.ForeignKey(verbose_name=b'Atendido por?', to_field=b'usuario', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.'),
        ),
    ]
