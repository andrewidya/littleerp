# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20161106_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='note',
            field=models.TextField(verbose_name=b'Notes', blank=True),
        ),
    ]
