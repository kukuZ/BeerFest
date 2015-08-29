# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0005_auto_20150617_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_category',
            name='last_flg',
            field=models.IntegerField(default=0),
        ),
    ]
