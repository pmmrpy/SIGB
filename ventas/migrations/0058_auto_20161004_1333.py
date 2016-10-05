# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0272_auto_20160827_2010'),
        ('ventas', '0057_auto_20161002_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='motivo_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='observaciones_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_pedido', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo el Pedido.', null=True, verbose_name=b'Cancelado por?'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario_modifica_pedido',
            field=models.ForeignKey(related_name='usuario_modifica_pedido', blank=True, to='personal.Empleado', help_text=b'Usuario que modifico el Pedido.', null=True, verbose_name=b'Modificado por?'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mozo_pedido',
            field=models.ForeignKey(verbose_name=b'Atendido por?', related_name=b'mozo_pedido', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.'),
        ),
    ]
