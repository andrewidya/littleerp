# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_auto_20160925_2023'),
        ('crm', '0013_auto_20160926_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(verbose_name='Visiting Date')),
                ('subject', models.CharField(max_length=255, verbose_name='Visit Subject Title')),
                ('employee', models.ManyToManyField(help_text='Personnels in the field when these visits', to='hrm.Employee', verbose_name='Personnels at Location')),
                ('sales_order_reference', models.ForeignKey(verbose_name='Sales Order', to='crm.SalesOrder', help_text='Sales Order number for referencing to customer')),
            ],
            options={
                'verbose_name': 'Visit Customer Information',
                'verbose_name_plural': 'Visit Customer Information',
            },
        ),
        migrations.CreateModel(
            name='VisitCustomerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report', models.CharField(max_length=255, verbose_name='Point Rate Item')),
                ('visit_customer', models.ForeignKey(verbose_name='Customer', to='operational.VisitCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='VisitPointRateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Point Rated Item',
                'verbose_name_plural': 'Point Rate Item Lists',
            },
        ),
        migrations.AddField(
            model_name='visitcustomerdetail',
            name='visit_point_rate_item',
            field=models.ForeignKey(verbose_name='Point Rate Item', to='operational.VisitPointRateItem'),
        ),
    ]
