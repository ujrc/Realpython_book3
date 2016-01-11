# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 5, 5, 19, 6, 915929, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusreport',
            name='when',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
