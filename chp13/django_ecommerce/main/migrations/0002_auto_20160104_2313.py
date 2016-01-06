# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 5, 5, 13, 42, 27673, tzinfo=utc)),
        ),
    ]
