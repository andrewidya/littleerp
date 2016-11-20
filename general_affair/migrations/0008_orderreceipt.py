# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0007_purchaseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReceipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='Receipt Number')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('receipt_date', models.DateField(verbose_name='Receipt Date')),
                ('purchase_order', models.ForeignKey(verbose_name='Purchase Order', to='general_affair.PurchaseOrder')),
            ],
            options={
                'verbose_name': 'Receipt Order',
                'verbose_name_plural': 'Order Receipt',
            },
        ),
    ]
