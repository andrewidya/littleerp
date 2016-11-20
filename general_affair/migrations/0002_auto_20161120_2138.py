# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SupplierBussinesType',
            new_name='SupplierBusinessType',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='bussiness_type',
            new_name='business_type',
        ),
    ]
