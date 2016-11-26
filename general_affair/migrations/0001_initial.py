# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Item')),
                ('code', models.CharField(unique=True, max_length=20, verbose_name='Code')),
                ('buy_price', models.DecimalField(verbose_name='Buy Price', max_digits=12, decimal_places=2)),
                ('sell_price', models.DecimalField(verbose_name='Sell Price', max_digits=12, decimal_places=2)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Item Lists & Stocks',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='ItemIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('date_issued', models.DateField(verbose_name='Date Issued')),
                ('recipient', models.CharField(max_length=255, verbose_name='Recipient')),
                ('allocation', models.CharField(max_length=255, verbose_name='Allocation')),
                ('item', models.ForeignKey(to='general_affair.Item')),
            ],
            options={
                'verbose_name': 'Item Issued',
                'verbose_name_plural': 'Item Issued',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=40, verbose_name='Code')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Item Type',
                'verbose_name_plural': 'Item Types',
            },
        ),
        migrations.CreateModel(
            name='OrderReceipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='Receipt Number')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('receipt_date', models.DateField(verbose_name='Receipt Date')),
            ],
            options={
                'verbose_name': 'Receipt Order',
                'verbose_name_plural': 'Order Receipt',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='PO Number')),
                ('order_date', models.DateField(verbose_name='Order Date')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('state', django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'ONGOING', b'ONGOING'), (b'CLOSE', b'CLOSE'), (b'CANCEL', b'CANCEL')])),
                ('item', models.ForeignKey(to='general_affair.Item')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Order',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Supplier Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address', blank=True)),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
                ('owner', models.CharField(max_length=50, verbose_name='Owner', blank=True)),
                ('tax_id_number', models.CharField(max_length=30, verbose_name='NPWP', blank=True)),
                ('owner_id_number', models.CharField(max_length=15, null=True, verbose_name='ID Number', blank=True)),
                ('siup_number', models.CharField(max_length=30, verbose_name='SIUP', blank=True)),
                ('tdp_number', models.CharField(max_length=30, verbose_name='TDP', blank=True)),
                ('join_date', models.DateField(null=True, verbose_name='Join Date', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='Start Date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='End Date', blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='SupplierBusinessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Bussiness Type')),
            ],
            options={
                'verbose_name': 'Supplier Bussiness Type',
                'verbose_name_plural': 'Supplier Bussiness Type',
            },
        ),
        migrations.AddField(
            model_name='supplier',
            name='business_type',
            field=models.ForeignKey(verbose_name='Bussiness Type', to='general_affair.SupplierBusinessType'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(to='general_affair.Supplier'),
        ),
        migrations.AddField(
            model_name='orderreceipt',
            name='purchase_order',
            field=models.ForeignKey(verbose_name='Purchase Order', to='general_affair.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(to='general_affair.ItemCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(to='general_affair.ItemType'),
        ),
    ]
