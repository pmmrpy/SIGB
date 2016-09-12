# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0175_auto_20160904_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagoproveedor',
            name='numero_nota_credito',
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='estado_linea_credito_proveedor',
            field=models.CharField(help_text=b'Se asigna automaticamente de acuerdo a la utilizacion de la Linea de Credito.', max_length=3, null=True, verbose_name=b'Estado Linea de Credito', choices=[(b'DEL', b'Dentro de la Linea de Credito'), (b'LIM', b'En el Limite'), (b'SOB', b'Sobregirada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 6, 18, 27, 51, 765000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='pagoproveedor',
            name='numero_comprobante_pago',
            field=models.IntegerField(default=0, help_text=b'Ingrese el Numero del Comprobante de Pago. El comprobante puede ser una Nota de Credito que anula o cancela la factura de la Compra en caso de que la misma se haya devuelto o cancelado.', verbose_name=b'Numero de Comprobante de Pago'),
        ),
    ]
