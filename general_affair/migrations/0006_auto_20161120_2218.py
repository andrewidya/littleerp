# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0005_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='ItemCategory',
            new_name='item_category',
        ),
    ]
