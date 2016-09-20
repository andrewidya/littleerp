# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20160920_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Item Category')),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='SalesOrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=3, verbose_name='Service Type', choices=[(b'1', b'Security'), (b'2', b'Office Boy'), (b'3', b'Administration')])),
                ('quantity', models.SmallIntegerField(verbose_name='Unit Quantity')),
                ('basic_salary', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'Sales Order Detail',
                'verbose_name_plural': 'Sales Order Details',
            },
        ),
        migrations.CreateModel(
            name='ServiceSalaryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name='Price', max_digits=12, decimal_places=2)),
                ('service_order_detail', models.ForeignKey(verbose_name='Service Order Detail', to='crm.SalesOrderDetail')),
            ],
            options={
                'verbose_name': 'Service Salary Detail',
                'verbose_name_plural': 'Service Salary Details',
            },
        ),
        migrations.CreateModel(
            name='ServiceSalaryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Price Item Component')),
                ('category', models.ForeignKey(related_name='service_price_item', verbose_name='Category', to='crm.ItemCategory')),
            ],
            options={
                'verbose_name': 'Service Salary Item',
                'verbose_name_plural': 'Service Salary Items',
            },
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='fee_calculate_condition',
            field=models.CharField(help_text='Set to basic if the fee will be calculated \t\tfrom basic salary, otherwise set to grand total', max_length=5, verbose_name='Fee Calculated Condition', choices=[(b'BASIC', b'Basic Salary'), (b'TOTAL', b'Grand Total')]),
        ),
        migrations.AddField(
            model_name='servicesalarydetail',
            name='service_salary_item',
            field=models.ForeignKey(verbose_name='Salary Item', to='crm.ServiceSalaryItem'),
        ),
        migrations.AddField(
            model_name='salesorderdetail',
            name='sales_order',
            field=models.ForeignKey(verbose_name='Sales Order Number', to='crm.SalesOrder'),
        ),
    ]
