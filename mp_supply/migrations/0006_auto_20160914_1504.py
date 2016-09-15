# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp_supply', '0005_auto_20160912_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='customer',
            field=models.ForeignKey(verbose_name='Work Location', to='crm.Customer'),
        ),
    ]
