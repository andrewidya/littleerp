# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Supplier Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address', blank=True)),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierBussinesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Bussiness Type')),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='bussiness_type',
            field=models.ForeignKey(verbose_name='Bussiness Type', to='general_affair.SupplierBussinesType'),
        ),
    ]
