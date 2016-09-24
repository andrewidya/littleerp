# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20160921_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Service Provided')),
            ],
            options={
                'verbose_name': 'Service Provided List',
            },
        ),
        migrations.AlterField(
            model_name='salesorderdetail',
            name='service',
            field=models.ForeignKey(verbose_name='Service Demand', to='crm.Service'),
        ),
    ]
