# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0006_auto_20161120_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='PO Number')),
                ('order_date', models.DateField(verbose_name='Order Date')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('state', django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'ONGOING', b'ONGOING'), (b'CLOSE', b'CLOSE')])),
                ('item', models.ForeignKey(to='general_affair.Item')),
                ('supplier', models.ForeignKey(to='general_affair.Supplier')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Order',
            },
        ),
    ]
