# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0009_auto_20161120_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('date_issued', models.DateField(verbose_name='Date Issued')),
                ('recipient', models.CharField(max_length=255, verbose_name='Recipient')),
                ('allocation', models.CharField(max_length=255, verbose_name='Allocation')),
                ('item', models.ForeignKey(to='general_affair.Item')),
            ],
            options={
                'verbose_name': 'Item Issued',
                'verbose_name_plural': 'Item Issued',
            },
        ),
    ]
