# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0004_auto_20150501_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='p_category',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='category',
        ),
        migrations.DeleteModel(
            name='Components',
        ),
        migrations.RemoveField(
            model_name='p_category',
            name='id_ctg',
        ),
        migrations.RemoveField(
            model_name='p_category',
            name='p_category',
        ),
        migrations.AddField(
            model_name='p_category',
            name='category_path',
            field=models.CharField(max_length=255, default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Commodity',
        ),
    ]
