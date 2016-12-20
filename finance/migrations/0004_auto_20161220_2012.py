# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20161220_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='ppn',
            field=models.DecimalField(default=Decimal('0.1000000000000000055511151231257827021181583404541015625'), help_text='PPN value must be decimal, ex: input 12\\% / as 0.12', verbose_name='PPN', max_digits=12, decimal_places=2),
        ),
    ]
