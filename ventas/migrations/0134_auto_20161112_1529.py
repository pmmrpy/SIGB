# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0133_auto_20161111_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 13, 4, 29, 8, 727000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 13, 4, 29, 8, 730000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente_documento_factura',
            field=models.CharField(default=1, help_text=b'Seleccione el Documento del Cliente el cual se registrara en la factura.', max_length=50, verbose_name=b'Documento Factura'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_pedido',
            field=models.ForeignKey(verbose_name=b'Numero de Pedido', blank=True, to='ventas.Pedido', help_text=b'Seleccione el Numero de Pedido para el cual se registrara la Venta.'),
        ),
    ]
