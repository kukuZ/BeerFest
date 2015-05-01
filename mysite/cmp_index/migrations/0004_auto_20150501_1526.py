# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0003_auto_20150430_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='num_compare',
            new_name='num_compared',
        ),
        migrations.RemoveField(
            model_name='category',
            name='num_elements',
        ),
    ]
