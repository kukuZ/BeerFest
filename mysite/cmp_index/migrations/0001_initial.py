# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('num_elements', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('num_viewer', models.IntegerField(default=0)),
                ('num_compare', models.IntegerField(default=0)),
                ('attribute', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('attribute', models.CharField(max_length=255)),
                ('id_attr', models.IntegerField()),
                ('category', models.ForeignKey(to='cmp_index.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('attribute', models.CharField(max_length=255)),
                ('id_attr', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='P_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('p_category', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='p_category',
            field=models.ForeignKey(to='cmp_index.P_Category'),
        ),
    ]
