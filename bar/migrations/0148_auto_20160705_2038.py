# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0147_auto_20160705_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compraestado',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='ordencompraestado',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='unidadmedidaproducto',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='caja',
            name='numero_caja',
            field=models.PositiveIntegerField(help_text=b'Ingrese el Numero de Caja.', verbose_name=b'Numero de Caja'),
        ),
        migrations.AlterField(
            model_name='cajaubicacion',
            name='caja_ubicacion',
            field=models.CharField(help_text=b'Ingrese un nombre o identificador de la ubicacion de la Caja. (Hasta 30 caracteres)', max_length=30, verbose_name=b'Ubicacion de la Caja'),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='categoria',
            field=models.CharField(help_text=b'Ingrese el identificador de la Categoria de los productos. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Categoria'),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la Categoria de los productos. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la Categoria'),
        ),
        migrations.AlterField(
            model_name='codigooperadoratelefono',
            name='codigo_operadora_telefono',
            field=models.IntegerField(help_text=b'Codigo de la Operadora de Telefonia.', verbose_name=b'Codigo Operadora'),
        ),
        migrations.AlterField(
            model_name='compraestado',
            name='estado_compra',
            field=models.CharField(max_length=3, verbose_name=b'Estado de la Compra', choices=[(b'PEN', b'Pendiente'), (b'CON', b'Confirmada'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cotizacion',
            field=models.DecimalField(help_text=b'Ingrese la Cotizacion en Guaranies de la Moneda.', max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 0, 38, 4, 380000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='deposito',
            field=models.CharField(help_text=b'Ingrese el identificador del Deposito. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Deposito'),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Deposito. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Deposito'),
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='plazo_compra',
            field=models.PositiveIntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo en dias para el pago.'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero_mesa',
            field=models.PositiveIntegerField(help_text=b'Ingrese el Numero de Mesa.', verbose_name=b'Numero de Mesa'),
        ),
        migrations.AlterField(
            model_name='mesaubicacion',
            name='mesa_ubicacion',
            field=models.CharField(help_text=b'Ingrese un nombre o identificador de la ubicacion de la Mesa. (Hasta 30 caracteres)', max_length=30, verbose_name=b'Ubicacion de la Mesa'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='abreviacion_moneda',
            field=models.CharField(help_text=b'Abreviacion o simbolo de la Moneda. EJ: Guaranies - Gs.', max_length=5, verbose_name=b'Abreviacion de la Moneda'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='codigo_moneda',
            field=models.IntegerField(help_text=b'Corresponde al codigo internacional de la Moneda. EJ: Gs - 600', verbose_name=b'Codigo de Moneda'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='moneda',
            field=models.CharField(help_text=b'Nombre de la Moneda.', max_length=100, verbose_name=b'Moneda'),
        ),
        migrations.AlterField(
            model_name='ordencompraestado',
            name='estado_orden_compra',
            field=models.CharField(max_length=3, verbose_name=b'Estado de la Orden de Compra', choices=[(b'EPP', b'En Proceso Proveedor'), (b'ENT', b'Entregada por el Proveedor'), (b'PEP', b'Pendiente de Entrega por el Proveedor'), (b'CAN', b'Cancelada')]),
        ),
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion de la SubCategoria de los productos. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion de la SubCategoria'),
        ),
        migrations.AlterField(
            model_name='subcategoriaproducto',
            name='subcategoria',
            field=models.CharField(help_text=b'Ingrese el identificador de la SubCategoria de los productos. (Hasta 2 caracteres)', max_length=2, verbose_name=b'SubCategoria'),
        ),
        migrations.AlterField(
            model_name='tipodeposito',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Tipo de Deposito. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Tipo de Deposito'),
        ),
        migrations.AlterField(
            model_name='tipodeposito',
            name='tipo_deposito',
            field=models.CharField(help_text=b'Ingrese el identificador del Tipo de Deposito. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Tipo de Deposito'),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='descripcion',
            field=models.CharField(help_text=b'', max_length=100, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='tipo_producto',
            field=models.CharField(help_text=b'', max_length=2, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='unidadmedidaproducto',
            name='unidad_medida_producto',
            field=models.CharField(max_length=2, choices=[(b'UN', b'Unidad'), (b'ML', b'Mililitros'), (b'GR', b'Gramos')]),
        ),
    ]
