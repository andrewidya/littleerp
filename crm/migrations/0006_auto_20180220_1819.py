# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20180217_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderdetail',
            name='basic_salary',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, blank=True, null=True, verbose_name='Base Salary'),
        ),
    ]
