# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp_supply', '0003_auto_20160912_0938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemcost',
            options={'verbose_name': 'Item Cost', 'verbose_name_plural': 'Item Costs'},
        ),
        migrations.AddField(
            model_name='salesorder',
            name='man_power_need',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
