# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_index', '0005_auto_20150617_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('attr_id', models.IntegerField(default=0)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date and time created', auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='date and time updated')),
                ('num_viewer', models.IntegerField(default=0)),
                ('p_category', models.ForeignKey(to='cmp_index.P_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('category', models.ForeignKey(related_name='commodities', to='cmp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('attributes', models.CommaSeparatedIntegerField(max_length=255)),
                ('id_attr', models.IntegerField()),
                ('category', models.ForeignKey(related_name='components', to='cmp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Scoreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('attr1_score', models.IntegerField(default=0)),
                ('attr2_score', models.IntegerField(default=0)),
                ('skip_cnt', models.IntegerField(default=0)),
                ('cannot_cnt', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date and time created', auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='date and time updated')),
                ('attr1_2', models.ManyToManyField(to='cmp.Attribute')),
                ('obj', models.ForeignKey(to='cmp.Commodity')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='obj',
            field=models.ForeignKey(to='cmp.Commodity'),
        ),
    ]
