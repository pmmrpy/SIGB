# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0175_auto_20160814_2240'),
        ('ventas', '0031_auto_20160814_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_encargada', models.CharField(max_length=3, choices=[(b'COC', b'Cocina'), (b'BAR', b'Barra')])),
                ('fecha_hora_pedido_comanda', models.DateTimeField()),
                ('estado_comanda', models.CharField(max_length=3, choices=[(b'PEN', b'Pendiente'), (b'PRO', b'Procesada'), (b'CAN', b'Cancelada')])),
                ('fecha_hora_procesamiento_comanda', models.DateTimeField()),
                ('producto_a_elaborar', models.ForeignKey(to='stock.ProductoCompuesto')),
            ],
            options={
                'verbose_name': 'Comanda',
                'verbose_name_plural': 'Comandas',
            },
        ),
    ]
