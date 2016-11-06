# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0031_auto_20161101_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='alpha_day',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'Day Alpha', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='l1',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'L1', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='l2',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'L2', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='l3',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'L3', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='l4',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'L4', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='leave_day',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'Leave Taken', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='leave_left',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'Leave Left', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='lk',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'LK', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='ln',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'LN', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='lp',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'LP', blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='sick_day',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'Day Sick', blank=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='normal_overtime',
            field=models.DecimalField(null=True, verbose_name=b'LN Rate', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='visitcustomer',
            name='employee',
            field=models.ManyToManyField(help_text='Personnels in the field when these visits', to='hrm.Employee', verbose_name='Personnels at Location'),
        ),
    ]
