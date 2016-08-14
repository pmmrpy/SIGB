# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0027_auto_20151108_2219'),
        ('compras', '0024_auto_20151108_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_compra', models.IntegerField(default=1, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, verbose_name=b'Numero Orden de Compra')),
                ('fecha_pedido', models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 19, 20, 129000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.')),
                ('fecha_entrega', models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 19, 20, 129000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.')),
                ('forma_pago', models.ForeignKey(default=1, to='bar.FormaPagoCompra', help_text=b'Seleccione la Forma de Pago para esta compra.')),
                ('proveedor_compra', models.ForeignKey(help_text=b'Seleccione el proveedor al cual se le realizara la compra.', to='compras.Proveedor')),
            ],
        ),
    ]
