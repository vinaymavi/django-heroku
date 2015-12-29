# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ert', '0003_auto_20151229_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='function_area',
            field=models.ForeignKey(default=None, to='ert.FunctionArea'),
            preserve_default=False,
        ),
    ]
