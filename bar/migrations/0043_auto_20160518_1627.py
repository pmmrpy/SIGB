# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0042_auto_20151215_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cajaestado',
            options={'verbose_name': 'Caja - Estado', 'verbose_name_plural': 'Cajas - Estados'},
        ),
        migrations.AlterModelOptions(
            name='cajaubicacion',
            options={'verbose_name': 'Caja - Ubicacion', 'verbose_name_plural': 'Cajas - Ubicaciones'},
        ),
        migrations.AlterModelOptions(
            name='categoriaproducto',
            options={'verbose_name': 'Producto - Categoria', 'verbose_name_plural': 'Productos - Categorias'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='codigociudadoperadoratelefono',
            options={'verbose_name': 'Telefono - Codigo por ciudad/operadora', 'verbose_name_plural': 'Telefonos - Codigos por ciudad/operadora'},
        ),
        migrations.AlterModelOptions(
            name='codigopaistelefono',
            options={'verbose_name': 'Telefono - Codigo intern. por pais', 'verbose_name_plural': 'Telefonos - Codigos intern. por pais'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'verbose_name': 'Cotizacion', 'verbose_name_plural': 'Cotizaciones'},
        ),
        migrations.AlterModelOptions(
            name='formapagocompra',
            options={'verbose_name': 'Forma de Pago - Compra', 'verbose_name_plural': 'Formas de Pago - Compra'},
        ),
        migrations.AlterModelOptions(
            name='formapagoventa',
            options={'verbose_name': 'Forma de Pago - Venta', 'verbose_name_plural': 'Formas de Pago - Venta'},
        ),
        migrations.AlterModelOptions(
            name='mesaestado',
            options={'verbose_name': 'Mesa - Estado', 'verbose_name_plural': 'Mesas - Estados'},
        ),
        migrations.AlterModelOptions(
            name='mesaubicacion',
            options={'verbose_name': 'Mesa - Ubicacion', 'verbose_name_plural': 'Mesas - Ubicaciones'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='reservaestado',
            options={'verbose_name': 'Reserva - Estado', 'verbose_name_plural': 'Reservas - Estados'},
        ),
        migrations.AlterModelOptions(
            name='tipodeposito',
            options={'verbose_name': 'Deposito - Tipo', 'verbose_name_plural': 'Depositos - Tipos'},
        ),
        migrations.AlterModelOptions(
            name='tipoproducto',
            options={'verbose_name': 'Producto - Tipo', 'verbose_name_plural': 'Productos - Tipos'},
        ),
        migrations.AlterField(
            model_name='codigopaistelefono',
            name='codigo_pais_telefono',
            field=models.IntegerField(help_text=b'Codigo internacional del pais al cual corresponde el telefono.', verbose_name=b'Codigo Pais'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 85000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='abreviacion_moneda',
            field=models.CharField(default=b'US$', help_text=b'Abreviacion o simbolo de la moneda. EJ: Guaranies - Gs.', max_length=5),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='codigo_moneda',
            field=models.IntegerField(help_text=b'Corresponde al codigo internacional de la moneda. EJ: Gs - 600'),
        ),
    ]
