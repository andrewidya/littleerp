# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='fee',
            field=models.DecimalField(decimal_places=3, max_digits=12, blank=True, help_text='Fee value must be decimal, ex: input 12\\% / as 0.12', null=True, verbose_name='Management Fee'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='pph21',
            field=models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text='PPh21 value must be decimal, ex: input 12\\% / as 0.12', null=True, verbose_name='PPh21'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='ppn',
            field=models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text='PPN value must be decimal, ex: input 12\\% / as 0.12', null=True, verbose_name='PPN'),
        ),
    ]
