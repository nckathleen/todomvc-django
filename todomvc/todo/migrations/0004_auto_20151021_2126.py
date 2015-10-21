# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20151021_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='order',
            field=models.SmallIntegerField(null=True),
        ),
    ]
