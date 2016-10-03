# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0042_auto_20160926_1901'),
        ('bar', '0288_auto_20160926_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='estado',
        ),
        migrations.AddField(
            model_name='caja',
            name='estado_caja',
            field=models.CharField(default=b'CER', help_text=b'Seleccione el identificador del Estado de la Caja.', max_length=3, verbose_name=b'Estado de la Caja', choices=[(b'ABI', b'Abierta'), (b'CER', b'Cerrada'), (b'CLA', b'Clausurada')]),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='venta',
            field=models.ForeignKey(default=1, to='ventas.Venta'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 9, 27, 13, 48, 19, 473000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.DeleteModel(
            name='CajaEstado',
        ),
    ]
