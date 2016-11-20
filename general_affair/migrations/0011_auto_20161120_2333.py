# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0010_itemissued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(unique=True, max_length=20, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='code',
            field=models.CharField(unique=True, max_length=40, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='orderreceipt',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='Receipt Number'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='PO Number'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='state',
            field=django_fsm.FSMField(default=b'DRAFT', max_length=50, choices=[(b'DRAFT', b'DRAFT'), (b'ONGOING', b'ONGOING'), (b'CLOSE', b'CLOSE'), (b'CANCEL', b'CANCEL')]),
        ),
    ]
