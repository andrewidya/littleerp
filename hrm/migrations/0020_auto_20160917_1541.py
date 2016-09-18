# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0019_auto_20160915_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(max_length=3, verbose_name='Status Pernikahan', choices=[(b'TK', b'Belum Menikah'), (b'K/0', b'Menikah Anak 0'), (b'K/1', b'Menikah Anak 1'), (b'K/2', b'Menikah Anak 2'), (b'K/3', b'Menikah Anak 3')]),
        ),
    ]
