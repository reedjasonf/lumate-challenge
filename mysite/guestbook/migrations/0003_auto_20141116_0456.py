# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20141116_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='sign_date',
            field=models.DateTimeField(verbose_name=b'date signed'),
            preserve_default=True,
        ),
    ]
