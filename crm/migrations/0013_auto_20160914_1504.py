# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20160914_1504'),
        ('mp_supply', '0006_auto_20160914_1504'),
        ('hrm', '0016_auto_20160914_1504'),
        ('crm', '0012_auto_20160912_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='parent',
            field=models.ForeignKey(blank=True, to='crm.Customer', null=True),
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
    ]
