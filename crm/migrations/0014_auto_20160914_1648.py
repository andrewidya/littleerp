# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20160914_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='parent',
            field=models.ForeignKey(verbose_name='Head Office', blank=True, to='crm.Customer', null=True),
        ),
    ]
