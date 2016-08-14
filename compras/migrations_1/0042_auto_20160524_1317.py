# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0044_auto_20160524_1317'),
        ('compras', '0041_auto_20160518_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaCreditoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_linea_credito_proveedor', models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 17, 4, 903000, tzinfo=utc), help_text=b'Ingrese la fecha en la quese registra la Linea deCredito ofrecida por el Proveedor.')),
                ('linea_credito_proveedor', models.IntegerField(help_text=b'Ingrese el monto ofrecido por el proveedor como Linea de Credito.')),
                ('estado_linea_credito_proveedor', models.BooleanField(help_text=b'')),
            ],
        ),
        # migrations.AddField(
            # model_name='compra',
            # name='estado_compra',
            # field=models.ForeignKey(default=b'EPP', to='bar.CompraEstado', help_text=b''),
        # ),
        migrations.AddField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 17, 4, 902000, tzinfo=utc), help_text=b'Ingrese la fecha en la que serealiza el alta del Proveedor.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 17, 17, 4, 906000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 17, 17, 4, 906000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_compra',
            field=models.IntegerField(default=1234567890, help_text=b'Este dato se genera automaticamente cada vez que se va crear una Orden de Compra.', unique=True, verbose_name=b'Numero Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='telefonoproveedor',
            name='contacto',
            field=models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero.(Hasta 100 caracteres)', max_length=100),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
    ]
