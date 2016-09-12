# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
            ],
            options={
                'verbose_name': 'Customer Branch Office',
                'verbose_name_plural': 'Customer Branch Offices',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('tax_id_number', models.CharField(max_length=30, verbose_name='NPWP')),
                ('join_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Customer List',
                'verbose_name_plural': 'Customer Information',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='customer',
            field=models.ForeignKey(to='crm.Customer'),
        ),
    ]
