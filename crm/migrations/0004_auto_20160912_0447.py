# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20160911_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='field',
            field=models.CharField(max_length=20, verbose_name='Field', blank=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='customer',
            field=models.ForeignKey(verbose_name='Head Office', to='crm.Customer'),
        ),
    ]
