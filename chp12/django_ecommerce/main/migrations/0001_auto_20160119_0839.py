# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', 'data_load_marketing_items_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 19, 14, 39, 17, 732707, tzinfo=utc)),
        ),
    ]
