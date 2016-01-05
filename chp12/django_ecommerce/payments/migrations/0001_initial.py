# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160104_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnpaidUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('last_notification', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('last_4_digits', models.CharField(blank=True, null=True, max_length=4)),
                ('stripe_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rank', models.CharField(default='Padwan', max_length=60)),
                ('badges', models.ManyToManyField(to='main.Badge')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
