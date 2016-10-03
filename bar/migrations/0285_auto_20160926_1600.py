# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0199_auto_20160925_1248'),
        ('bar', '0284_auto_20160926_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamaraFrigorifica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camara', models.CharField(max_length=50, verbose_name=b'Descripcion del Nivel')),
                ('capacidad', models.PositiveIntegerField()),
                ('capacidad_ocupada', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estante', models.CharField(max_length=50, verbose_name=b'Descripcion del Estante')),
            ],
        ),
        migrations.CreateModel(
            name='Hilera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hilera', models.CharField(max_length=50, verbose_name=b'Descripcion de la Hilera')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=50, verbose_name=b'Descripcion del Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Pasillo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pasillo', models.CharField(max_length=50, verbose_name=b'Descripcion del Pasillo')),
            ],
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('piso', models.CharField(max_length=50, verbose_name=b'Descripcion del Piso')),
            ],
        ),
        migrations.AddField(
            model_name='deposito',
            name='estante',
            field=models.PositiveIntegerField(default=5, verbose_name=b'Cantidad de Estantes'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='hilera',
            field=models.PositiveIntegerField(default=10, verbose_name=b'Cantidad de Hileras'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='nivel',
            field=models.PositiveIntegerField(default=5, verbose_name=b'Cantidad de Niveles'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='pasillo',
            field=models.PositiveIntegerField(default=3, verbose_name=b'Cantidad de Pasillos'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='piso',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Cantidad de Pisos'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 9, 26, 16, 0, 33, 675000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AddField(
            model_name='piso',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_piso', to='bar.Deposito'),
        ),
        migrations.AddField(
            model_name='pasillo',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_pasillo', to='bar.Deposito'),
        ),
        migrations.AddField(
            model_name='pasillo',
            name='piso',
            field=models.ForeignKey(to='bar.Piso'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_nivel', to='bar.Deposito'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='estante',
            field=models.ForeignKey(to='bar.Estante'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='pasillo',
            field=models.ForeignKey(to='bar.Pasillo'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='piso',
            field=models.ForeignKey(to='bar.Piso'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_hilera', to='bar.Deposito'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='estante',
            field=models.ForeignKey(to='bar.Estante'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='nivel',
            field=models.ForeignKey(to='bar.Nivel'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='pasillo',
            field=models.ForeignKey(to='bar.Pasillo'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='piso',
            field=models.ForeignKey(to='bar.Piso'),
        ),
        migrations.AddField(
            model_name='hilera',
            name='producto',
            field=models.ForeignKey(to='stock.Producto'),
        ),
        migrations.AddField(
            model_name='estante',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_estante', to='bar.Deposito'),
        ),
        migrations.AddField(
            model_name='estante',
            name='pasillo',
            field=models.ForeignKey(to='bar.Pasillo'),
        ),
        migrations.AddField(
            model_name='estante',
            name='piso',
            field=models.ForeignKey(to='bar.Piso'),
        ),
        migrations.AddField(
            model_name='camarafrigorifica',
            name='deposito',
            field=models.ForeignKey(related_name='deposito_camara_frigorifica', to='bar.Deposito'),
        ),
    ]
