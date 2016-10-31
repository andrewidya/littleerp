# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0029_auto_20161031_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='l1',
            field=models.PositiveIntegerField(null=True, verbose_name=b'L1', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='l2',
            field=models.PositiveIntegerField(null=True, verbose_name=b'L2', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='l3',
            field=models.PositiveIntegerField(null=True, verbose_name=b'L3', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='l4',
            field=models.PositiveIntegerField(null=True, verbose_name=b'L4', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lk',
            field=models.PositiveIntegerField(null=True, verbose_name=b'LK', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='ln',
            field=models.PositiveIntegerField(null=True, verbose_name=b'LN', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lp',
            field=models.PositiveIntegerField(null=True, verbose_name=b'LP', blank=True),
        ),
    ]
