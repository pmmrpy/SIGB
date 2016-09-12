# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0177_auto_20160905_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora Compra', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='facturaproveedor',
            name='estado_factura_compra',
            field=models.CharField(blank=True, help_text=b'Indique el Estado de la Factura de la Compra de acuerdo a los pagos aplicados para la misma.', max_length=3, verbose_name=b'Estado de la Factura Compra', choices=[(b'EPP', b'En Plazo de Pago'), (b'FPP', b'Fuera del Plazo de Pago'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 8, 19, 40, 53, 366000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='proveedortelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo Operadora', to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione o ingrese el codigo de ciudad u operadora de telefonia movil.'),
        ),
        migrations.AlterField(
            model_name='proveedortelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo Pais', to='bar.CodigoPaisTelefono'),
        ),
        migrations.AlterField(
            model_name='proveedortelefono',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del Proveedor. El dato debe contener solo numeros.'),
        ),
    ]
