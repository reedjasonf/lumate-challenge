# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_auto_20141116_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='ip',
            field=models.CharField(default='0.0.0.0', max_length=16),
            preserve_default=False,
        ),
    ]
