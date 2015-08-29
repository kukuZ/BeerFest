# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='p_category',
            field=models.ForeignKey(to='cmp_index.P_Category', related_name='p_category'),
        ),
    ]
