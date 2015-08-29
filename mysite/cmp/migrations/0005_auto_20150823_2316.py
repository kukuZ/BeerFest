# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0004_category_link_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='attr_id',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='name',
        ),
        migrations.RemoveField(
            model_name='components',
            name='id_attr',
        ),
        migrations.AlterField(
            model_name='attribute',
            name='obj',
            field=models.ForeignKey(to='cmp.Commodity', related_name='attribute'),
        ),
        migrations.RemoveField(
            model_name='components',
            name='attributes',
        ),
        migrations.AddField(
            model_name='attribute',
            name='attr_name',
            field=models.ForeignKey(to='cmp.AttributeList', default=0, related_name='commodity'),
        ),
        migrations.AddField(
            model_name='components',
            name='attributes',
            field=models.ManyToManyField(to='cmp.AttributeList'),
        ),
    ]
