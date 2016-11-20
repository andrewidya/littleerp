# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0008_orderreceipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='buy_price',
            field=models.DecimalField(default=1, verbose_name='Buy Price', max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='code',
            field=models.CharField(default='A.1', max_length=20, verbose_name='Code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='sell_price',
            field=models.DecimalField(default=12000, verbose_name='Sell Price', max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]
