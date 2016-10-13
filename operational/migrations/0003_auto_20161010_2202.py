# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0002_auto_20161010_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payrollperiod',
            options={'verbose_name': 'Period', 'verbose_name_plural': 'Peroids'},
        ),
        migrations.AddField(
            model_name='payrollperiod',
            name='period',
            field=models.CharField(default=datetime.datetime(2016, 10, 10, 15, 2, 9, 14236, tzinfo=utc), max_length=15, verbose_name=b'Month'),
            preserve_default=False,
        ),
    ]
