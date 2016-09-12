# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0030_auto_20160814_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoValorCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovimientoCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='RetiroValorCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cocina',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mozo_pedido',
            field=models.ForeignKey(verbose_name=b'Atendido por?', to='personal.Empleado', help_text=b'Este dato se completara automaticamente cuando el Pedido sea guardado.'),
        ),
        migrations.AlterField(
            model_name='pedidodetalle',
            name='precio_producto_pedido',
            field=models.DecimalField(help_text=b'El Precio de Venta del Producto se define en la pantalla de Productos.', verbose_name=b'Precio Venta Producto', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='precio_producto_venta',
            field=models.DecimalField(help_text=b'El Precio de Venta del Producto se define en la pantalla de Productos.', verbose_name=b'Precio Venta Producto', max_digits=18, decimal_places=0),
        ),
    ]
