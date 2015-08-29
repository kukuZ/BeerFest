# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_auto_20150706_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='p_category',
        ),
    ]
