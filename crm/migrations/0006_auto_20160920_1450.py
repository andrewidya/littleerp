# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20160920_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='reference',
            field=models.CharField(max_length=255, verbose_name='Reference', blank=True),
        ),
    ]
