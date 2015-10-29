# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flaggedcontent',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
