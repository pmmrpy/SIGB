# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0171_auto_20160828_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='empresa_administrada',
            field=models.BooleanField(default=False, help_text=b'Diferencia las empresas administradas de las proveedoras.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_orden_compra',
            field=models.ForeignKey(default=1, verbose_name=b'Estado', to='bar.OrdenCompraEstado', help_text=b'El estado de la Orden de Compra se establece automaticamente de acuerdo a la Fecha de Entrega ingresada.'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 31, 23, 17, 2, 722000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='total_orden_compra',
            field=models.DecimalField(default=0, verbose_name=b'Total', max_digits=18, decimal_places=0),
        ),
    ]
