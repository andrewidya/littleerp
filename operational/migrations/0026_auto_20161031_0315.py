# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operational', '0025_auto_20161030_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='staff',
            field=models.ForeignKey(verbose_name=b'User Staff', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='total',
            field=models.DecimalField(null=True, verbose_name=b'Total Salary', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
