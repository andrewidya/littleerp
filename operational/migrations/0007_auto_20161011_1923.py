# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0006_auto_20161011_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payrollperiod',
            options={'verbose_name': 'Period', 'verbose_name_plural': 'Periods'},
        ),
        migrations.AlterField(
            model_name='attendance',
            name='alpha_day',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Day Alpha', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='leave_day',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Leave Taken', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='leave_left',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Leave Left', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='sick_day',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Day Sick', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='work_day',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Day Work', blank=True),
        ),
    ]
