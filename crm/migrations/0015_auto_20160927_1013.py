# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20160927_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='satisfication',
            options={'verbose_name': 'Satisfication', 'verbose_name_plural': 'Satisfication Interview'},
        ),
        migrations.AddField(
            model_name='satisficationdetail',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satisficationdetail',
            name='value',
            field=models.DecimalField(verbose_name='Point', max_digits=1, decimal_places=0),
        ),
    ]
