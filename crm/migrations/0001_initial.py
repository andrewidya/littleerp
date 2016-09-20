# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
                ('address', models.CharField(max_length=100, verbose_name='Address', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name='City', blank=True)),
                ('field', models.CharField(max_length=20, verbose_name='Field', blank=True)),
                ('tax_id_number', models.CharField(max_length=30, verbose_name='NPWP', blank=True)),
                ('join_date', models.DateField()),
                ('parent', models.ForeignKey(verbose_name='Head Office', blank=True, to='crm.Customer', null=True)),
            ],
            options={
                'verbose_name': 'Customer List',
                'verbose_name_plural': 'Customer Information',
                'permissions': (('view_only_customer', 'Can view only available customer'),),
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(verbose_name='Date Issued')),
                ('date_start', models.DateField(verbose_name='Contract Start Date')),
                ('date_end', models.DateField(verbose_name='Contract End Date')),
                ('reference', models.CharField(max_length=255, verbose_name='Reference')),
                ('note', models.TextField()),
                ('tax', models.DecimalField(help_text='Tax value must be decimal, ex: input 12\\% / as 0.12', verbose_name='Tax', max_digits=12, decimal_places=2)),
                ('fee', models.DecimalField(verbose_name='Management Fee', max_digits=12, decimal_places=2)),
                ('fee_calculate_condition', models.CharField(help_text='Set to basic if the fee will be calculated \t\tfrom basic salary, otherwise set to grand total', max_length=5, verbose_name='Fee Calculated Condition')),
                ('customer', models.ForeignKey(verbose_name='Customer Name', to='crm.Customer')),
            ],
        ),
    ]
