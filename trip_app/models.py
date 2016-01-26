from django.db import models
from datetime import datetime
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

from custom_auth.models import MyUser


# Create your models here.
class Trip(models.Model):
	user = models.ForeignKey(MyUser, related_name = 'trip_user')
	trip_name = models.CharField(max_length = 256)
	trip_location = models.CharField(max_length = 256)
	trip_description = models.TextField(max_length = 1024, blank = True)
	total_expenses = models.DecimalField(default =	Decimal('0.00'), max_digits = 19, decimal_places = 2,validators=[MinValueValidator(0)])
	start_date = models.DateField()
	end_date = models.DateField()

	def __unicode__(self):
		return self.trip_name


class Activity(models.Model):
	trip = models.ForeignKey(Trip, related_name = 'trip_activ')
	activ_name = models.CharField(max_length = 256)
	activ_location = models.CharField(max_length = 256)
	activ_description = models.TextField(max_length = 1024, blank = True)
	expenses = models.DecimalField(default =	Decimal('0.00'), max_digits = 19, decimal_places = 2,validators=[MinValueValidator(0)])
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField()

	def __unicode__(self):
		return self.activ_name

	def save(self):
		super(Activity, self).save()
		activ_expenses = Activity.objects.filter(trip = self.trip)
		total = 0
		for i_expenses in activ_expenses:
			total += i_expenses.expenses
		self.trip.total_expenses = total
		super(Trip, self.trip).save()