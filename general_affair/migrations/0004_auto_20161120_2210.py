# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0003_auto_20161120_2146'),
    ]

    operations = [
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
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=40, verbose_name='Code')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Item Type',
                'verbose_name_plural': 'Item Types',
            },
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
        migrations.AlterModelOptions(
            name='supplierbusinesstype',
            options={'verbose_name': 'Supplier Bussiness Type', 'verbose_name_plural': 'Supplier Bussiness Type'},
        ),
    ]
