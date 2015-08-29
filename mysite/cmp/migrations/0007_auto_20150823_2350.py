# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0006_auto_20150823_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='text',
        ),
        migrations.AddField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=255, default='None:None'),
        ),
    ]
