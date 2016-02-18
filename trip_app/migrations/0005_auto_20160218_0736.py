# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0004_auto_20160218_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 18, 7, 36, 30, 107669)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
