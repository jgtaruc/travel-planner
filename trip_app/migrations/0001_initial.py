# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activ_name', models.CharField(max_length=256)),
                ('activ_location', models.CharField(max_length=256)),
                ('activ_description', models.TextField(max_length=1024, blank=True)),
                ('expenses', models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_name', models.CharField(max_length=256)),
                ('trip_location', models.CharField(max_length=256)),
                ('trip_description', models.TextField(max_length=1024, blank=True)),
                ('total_expenses', models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(related_name='trip_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='trip',
            field=models.ForeignKey(related_name='trip_activ', to='trip_app.Trip'),
        ),
    ]
