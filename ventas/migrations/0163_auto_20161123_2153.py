# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from decimal import Decimal
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0162_auto_20161121_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta con Pedido', 'verbose_name_plural': 'Ventas con Pedido'},
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='id_mov_stock',
            field=models.PositiveIntegerField(help_text=b'Registra el dato del ID MovimientoStock para poder recuperar los datos necesarios para realizar la reversion de los descuentos de Stock cuando se cancela un Producto o todo el Pedido en la pantalla de Pedidos.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='fecha_hora_fin_apertura_caja',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 10, 53, 13, 732000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Apertura de Caja.', verbose_name=b'Fecha/hora Fin Apertura Caja'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='cantidad_solicitada',
            field=models.DecimalField(default=1, verbose_name=b'Cantidad Solicitada', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='fecha_hora_fin_jornada',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 10, 53, 13, 735000, tzinfo=utc), help_text=b'Fecha/hora de Finalizacion de la Jornada.', verbose_name=b'Fecha/hora Fin Jornada'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='cantidad_producto_venta',
            field=models.DecimalField(help_text=b'Ingrese la cantidad del producto solicitada por el Cliente.', verbose_name=b'Cantidad del Producto', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(Decimal('0.001'))]),
        ),
    ]
