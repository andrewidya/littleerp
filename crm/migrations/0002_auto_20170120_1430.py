# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic_name',
            field=models.CharField(max_length=15, null=True, verbose_name='Person In Charge', blank=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='contract',
            field=models.CharField(max_length=255, verbose_name='Contract Ref', blank=True),
        ),
    ]
