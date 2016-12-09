# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Availability'),
        ),
        migrations.AlterField(
            model_name='itemissued',
            name='item',
            field=models.ForeignKey(to='general_affair.Item', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='orderreceipt',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Purchase Order', to='general_affair.PurchaseOrder'),
        ),
    ]
