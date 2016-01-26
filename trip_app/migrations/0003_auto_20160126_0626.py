# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0002_auto_20160126_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='expenses',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='total_expenses',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=19, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
