# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_auto_20160927_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='blood_type',
            field=models.CharField(blank=True, max_length=2, verbose_name='Blood Type', choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last Name', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mother_name',
            field=models.CharField(max_length=30, verbose_name='Mother Name', blank=True),
        ),
    ]
