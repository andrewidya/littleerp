# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_auto_20161028_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=models.ImageField(upload_to=b'crm/customer/logo/%Y/%m/%d', null=True, verbose_name=b'Logo', blank=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='fee_calculate_condition',
            field=models.CharField(help_text='Set to basic if the fee will be calculated from basic salary, otherwise set to grand total', max_length=5, verbose_name='Fee Calculated Condition', choices=[(b'BASIC', b'Basic Salary'), (b'TOTAL', b'Grand Total')]),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='tax',
            field=models.DecimalField(help_text='Tax value must be decimal, ex: input 12\\% / as 0.12', verbose_name='Tax', max_digits=12, decimal_places=2),
        ),
    ]
