# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0003_auto_20160126_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 18, 7, 34, 6, 627392)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 18, 7, 34, 6, 627371)),
        ),
    ]
