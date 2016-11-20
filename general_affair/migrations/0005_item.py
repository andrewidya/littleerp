# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0004_auto_20161120_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Item')),
                ('description', models.TextField(blank=True)),
                ('ItemCategory', models.ForeignKey(to='general_affair.ItemCategory')),
                ('item_type', models.ForeignKey(to='general_affair.ItemType')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Item Lists & Stocks',
            },
        ),
    ]
