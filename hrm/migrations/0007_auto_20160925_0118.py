# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0006_auto_20160924_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Bank Name')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='bank',
            field=models.ForeignKey(default=1, verbose_name='Bank', to='hrm.BankName'),
            preserve_default=False,
        ),
    ]
