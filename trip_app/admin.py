from django.contrib import admin
from trip_app.models import Trip, Activity


# Register your models here.
class Activ_Inline(admin.StackedInline):
	model = Activity
	extra = 0


class Trip_Admin(admin.ModelAdmin):
	model = Trip
	inlines = [Activ_Inline]
	def save_model(self, request, obj, form, change):
		i_expenses = Activity.objects.filter(trip = obj.pk)





admin.site.register(Trip, Trip_Admin)