# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0005_auto_20150823_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attr_name',
            field=models.ForeignKey(to='cmp.AttributeList', related_name='commodity'),
        ),
    ]
