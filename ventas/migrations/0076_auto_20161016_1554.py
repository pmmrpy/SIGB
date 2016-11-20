# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0075_auto_20161016_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comanda',
            old_name='tiempo_estimado_elaboracion',
            new_name='tiempo_estimado_procesamiento',
        ),
        migrations.AlterField(
            model_name='comanda',
            name='area_solicitante',
            field=models.ForeignKey(related_name='area_solicitante_comanda', verbose_name=b'Area Solicitante', to='bar.Sector'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='fecha_hora_pedido_comanda',
            field=models.DateTimeField(verbose_name=b'Fecha/hora Comanda'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='numero_pedido',
            field=models.ForeignKey(verbose_name=b'Numero de Pedido', to='ventas.Pedido'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='producto_a_entregar',
            field=models.ForeignKey(verbose_name=b'Producto Solicitado', to='stock.ProductoVenta'),
        ),
    ]
