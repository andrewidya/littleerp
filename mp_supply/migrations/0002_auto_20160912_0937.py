# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp_supply', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdetail',
            name='item_cost',
        ),
        migrations.AddField(
            model_name='salesorder',
            name='item_cost',
            field=models.ManyToManyField(to='mp_supply.ItemDetail', through='mp_supply.ItemCost'),
        ),
    ]
