# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0002_p_category_id_ctg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='attribute',
            field=models.CharField(max_length=255),
        ),
    ]
