# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_remove_satisficationdetail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisficationpointrateitem',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
    ]
