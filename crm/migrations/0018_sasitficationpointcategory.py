# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20160927_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='SasitficationPointCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Satisfication Point Category')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Satisfication Point Category',
                'verbose_name_plural': 'Satisfication Point Categories',
            },
        ),
    ]
