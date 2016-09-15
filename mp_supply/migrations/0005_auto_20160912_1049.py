# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp_supply', '0004_auto_20160912_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='man_power_need',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
