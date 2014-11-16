# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='sign_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date signed'),
            preserve_default=True,
        ),
    ]
