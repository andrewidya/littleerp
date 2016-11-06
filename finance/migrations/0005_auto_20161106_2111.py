# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20161106_2046'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='invoicedetail',
            unique_together=set([('invoiced_item', 'period')]),
        ),
    ]
