# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_auto_20160927_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='fee_calculate_condition',
            field=models.CharField(help_text='Set to basic if \t\t\t\t\t\t\t\t\t\t\t  \t\t\t the fee will be \t\t\t\t\t\t\t\t\t\t\t  \t\t\t calculated from \t\t\t\t\t\t\t\t\t\t\t  \t\t\t basic salary, \t\t\t\t\t\t\t\t\t\t\t  \t\t\t otherwise set \t\t\t\t\t\t\t\t\t\t\t  \t\t\t to grand total', max_length=5, verbose_name='Fee Calculated \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Condition', choices=[(b'BASIC', b'Basic Salary'), (b'TOTAL', b'Grand Total')]),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='tax',
            field=models.DecimalField(help_text='Tax value must be decimal, \t\t\t\t\t\t\t \t\t\tex: input 12\\% / as 0.12', verbose_name='Tax', max_digits=12, decimal_places=2),
        ),
    ]
