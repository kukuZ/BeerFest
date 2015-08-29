# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0006_p_category_last_flg'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_category',
            name='category_id',
            field=models.IntegerField(default=0),
        ),
    ]
