# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0007_auto_20150823_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreset',
            name='attr1_2',
        ),
        migrations.RemoveField(
            model_name='scoreset',
            name='obj',
        ),
        migrations.AddField(
            model_name='scoreset',
            name='obj1',
            field=models.ForeignKey(default=0, related_name='obj1_for_score', to='cmp.Commodity'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='obj1_attr',
            field=models.ForeignKey(default=0, related_name='obj1s_attr_for_score', to='cmp.Attribute'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='obj2',
            field=models.ForeignKey(default=0, related_name='obj2_for_score', to='cmp.Commodity'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='obj2_attr',
            field=models.ForeignKey(default=0, related_name='obj2s_attr_for_score', to='cmp.Attribute'),
        ),
    ]
