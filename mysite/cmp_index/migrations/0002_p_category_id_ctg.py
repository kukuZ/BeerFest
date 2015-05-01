# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_category',
            name='id_ctg',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
