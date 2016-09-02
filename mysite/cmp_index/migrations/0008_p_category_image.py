# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0007_p_category_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_category',
            name='image',
            field=models.ImageField(blank=True, upload_to='P_Category/', null=True),
        ),
    ]
