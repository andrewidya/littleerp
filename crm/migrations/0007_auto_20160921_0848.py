# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20160920_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(unique=True, max_length=10, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='salesorderdetail',
            name='service',
            field=models.CharField(max_length=3, verbose_name='Service Type', choices=[(b'SCR', b'Security'), (b'OFB', b'Office Boy'), (b'ADM', b'Administration')]),
        ),
    ]
