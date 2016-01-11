# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=350)),
                ('votes', models.IntegerField(default=0)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5, default=0.0)),
                ('poll', models.ForeignKey(to='djangular_polls.Poll', related_name='items')),
            ],
            options={
                'ordering': ['-text'],
            },
        ),
    ]
