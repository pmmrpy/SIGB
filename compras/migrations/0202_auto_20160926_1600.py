# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0201_auto_20160926_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 27, 20, 0, 33, 700000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='usuario_modifica_orden_compra',
            field=models.ForeignKey(related_name='usuario_modifica', blank=True, to='personal.Empleado', help_text=b'Usuario que modifico la Orden de Compra.', null=True, verbose_name=b'Modificado por?'),
        ),
    ]
