from __future__ import unicode_literals
from django.db import migrations
from datetime import datetime


def migrate_bigcorpid(apps,schema_editor):
    User = apps.get_model('payments', 'User')
    for u in User.objects.all():
        bigcoid=("%s%s%s" % (u.name[:2],
                                u.rank[:1],
                                u.created_at.strftime("%Y%m%d%H%M%S%f"),
                                ))
        u.bigCorpID=bigcoid
        u.save()

class Migration(migrations.Migration):
    dependencies = [
    ('payments', '0004_user_bigcorpid'),
    ]

    operations = [
    migrations.RunPython(migrate_bigcorpid)
    ]
