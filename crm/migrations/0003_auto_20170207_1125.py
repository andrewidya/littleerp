# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170120_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='parent',
            field=models.ForeignKey(verbose_name='PIC', blank=True, to='crm.Customer', null=True),
        ),
    ]
