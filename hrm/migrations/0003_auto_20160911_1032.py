# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_auto_20160911_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='division',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
