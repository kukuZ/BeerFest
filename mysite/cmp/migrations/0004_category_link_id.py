# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0003_remove_category_p_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='link_id',
            field=models.IntegerField(default=0),
        ),
    ]
