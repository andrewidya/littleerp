# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salesorder',
            options={'verbose_name': 'Sales Order', 'verbose_name_plural': 'Sales Orders'},
        ),
        migrations.AddField(
            model_name='salesorder',
            name='number',
            field=models.CharField(default='', max_length=50, verbose_name='SO Number'),
            preserve_default=False,
        ),
    ]
