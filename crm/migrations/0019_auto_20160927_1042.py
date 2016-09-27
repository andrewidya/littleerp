# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_sasitficationpointcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SasitficationPointCategory',
            new_name='SatisficationPointCategory',
        ),
        migrations.AddField(
            model_name='satisficationpointrateitem',
            name='category',
            field=models.ForeignKey(default='', verbose_name='Point Category', to='crm.SatisficationPointCategory'),
            preserve_default=False,
        ),
    ]
