# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0169_auto_20160827_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagoproveedor',
            name='procesado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
            field=models.CharField(default=b'EPP', help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura Compra', choices=[(b'EPP', b'En Plazo de Pago'), (b'FPP', b'Fuera del Plazo de Pago'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 30, 0, 10, 13, 614000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompradetalle',
            name='unidad_medida_orden_compra',
            field=models.ForeignKey(verbose_name=b'Unidad de Medida del Producto', to='bar.UnidadMedidaProducto', help_text=b'Debe ser la definida en los datos del Producto, no debe ser seleccionada por el usuario.'),
        ),
        migrations.AlterUniqueTogether(
            name='facturaproveedor',
            unique_together=set([('proveedor', 'numero_factura_compra')]),
        ),
    ]
