# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20160925_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicesalaryitem',
            options={'verbose_name': 'Service Salary Item', 'verbose_name_plural': 'Service Salariy Items'},
        ),
        migrations.AlterField(
            model_name='salesorderdetail',
            name='sales_order',
            field=models.ForeignKey(related_name='sales_order', verbose_name='Sales Order Number', to='crm.SalesOrder'),
        ),
    ]
