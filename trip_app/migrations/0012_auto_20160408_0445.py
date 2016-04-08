# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0011_auto_20160218_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='activity',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
