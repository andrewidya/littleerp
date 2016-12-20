# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20161220_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='ppn',
            field=models.DecimalField(default=0.1, help_text='PPN value must be decimal, ex: input 12\\% / as 0.12', verbose_name='PPN', max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]
