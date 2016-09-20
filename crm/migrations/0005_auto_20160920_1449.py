# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_salesorderdetail_other_salary_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='fee',
            field=models.DecimalField(verbose_name='Management Fee', max_digits=12, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='number',
            field=models.CharField(max_length=50, verbose_name='SO Number', blank=True),
        ),
    ]
