# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        #('payments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 5, 5, 13, 34, 944618, tzinfo=utc))),
                ('image', models.CharField(null=True, max_length=300)),
                ('vid', models.URLField(null=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MarketingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('img_name', models.CharField(max_length=250)),
                ('heading', models.CharField(max_length=320)),
                ('caption', models.TextField()),
                ('button_title', models.CharField(default=' View details', max_length=25)),
                ('button_link', models.URLField(null=True, default='register')),
            ],
        ),
        # migrations.CreateModel(
        #     name='StatusReport',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
        #         ('when', models.DateTimeField(auto_now_add=True)),
        #         ('status', models.CharField(max_length=200)),
        #         ('user', models.ForeignKey(to='payments.User')),
        #     ],
        # ),
    ]
