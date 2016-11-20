# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0323_auto_20161013_1959'),
        ('personal', '0274_auto_20161010_1636'),
        ('ventas', '0066_comanda_area_encargada'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='area_solicitante',
            field=models.ForeignKey(related_name='area_solicitante_comanda', default=2, verbose_name=b'Area Encargada', to='bar.Sector'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='usuario_procesa',
            field=models.ForeignKey(related_name='usuario_procesa_comanda', blank=True, to='personal.Empleado', help_text=b'Usuario que proceso la Comanda.', null=True, verbose_name=b'Procesado por?'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='usuario_solicitante',
            field=models.ForeignKey(related_name='usuario_solicitante_comanda', default=14, verbose_name=b'Solicitado por?', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='area_encargada',
            field=models.ForeignKey(related_name='area_encargada_comanda', verbose_name=b'Area Encargada', to='bar.Sector'),
        ),
    ]
