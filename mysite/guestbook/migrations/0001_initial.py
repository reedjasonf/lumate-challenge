# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=192)),
                ('last_name', models.CharField(max_length=192)),
                ('sign_date', models.DateTimeField(auto_now=True, verbose_name=b'date signed', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
