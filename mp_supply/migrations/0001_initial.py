# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20160912_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='ItemCost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(to='mp_supply.ItemCategory')),
            ],
            options={
                'verbose_name': 'Item Detail',
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('so_number', models.CharField(max_length=50, verbose_name='Sales Order Number')),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(to='crm.Branch')),
            ],
            options={
                'verbose_name': 'Sales Order',
            },
        ),
        migrations.AddField(
            model_name='itemdetail',
            name='item_cost',
            field=models.ManyToManyField(to='mp_supply.SalesOrder', through='mp_supply.ItemCost'),
        ),
        migrations.AddField(
            model_name='itemcost',
            name='item_detail',
            field=models.ForeignKey(to='mp_supply.ItemDetail'),
        ),
        migrations.AddField(
            model_name='itemcost',
            name='sales_order',
            field=models.ForeignKey(to='mp_supply.SalesOrder'),
        ),
    ]
