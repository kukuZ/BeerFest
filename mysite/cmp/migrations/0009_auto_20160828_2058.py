# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0008_auto_20150824_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='image',
            field=models.ImageField(blank=True, upload_to='Commodity/', null=True),
        ),
        migrations.AlterField(
            model_name='scoreset',
            name='obj1',
            field=models.ForeignKey(to='cmp.Commodity', related_name='obj1_for_score'),
        ),
        migrations.AlterField(
            model_name='scoreset',
            name='obj1_attr',
            field=models.ForeignKey(to='cmp.Attribute', related_name='obj1s_attr_for_score'),
        ),
        migrations.AlterField(
            model_name='scoreset',
            name='obj2',
            field=models.ForeignKey(to='cmp.Commodity', related_name='obj2_for_score'),
        ),
        migrations.AlterField(
            model_name='scoreset',
            name='obj2_attr',
            field=models.ForeignKey(to='cmp.Attribute', related_name='obj2s_attr_for_score'),
        ),
    ]
