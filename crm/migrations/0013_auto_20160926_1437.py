# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20160925_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderdetail',
            name='sales_order',
            field=models.ForeignKey(verbose_name='Sales Order Number', to='crm.SalesOrder'),
        ),
    ]
