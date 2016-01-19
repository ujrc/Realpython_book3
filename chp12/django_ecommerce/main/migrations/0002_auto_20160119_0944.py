# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_auto_20160119_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 19, 15, 44, 7, 101328, tzinfo=utc)),
        ),
    ]
