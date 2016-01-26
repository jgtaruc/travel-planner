from django.contrib import admin
from django.db.models import signals
from trip_app.models import Trip, Activity


# Register your models here.
class Activ_Inline(admin.StackedInline):
	model = Activity
	extra = 0


class Trip_Admin(admin.ModelAdmin):
	model = Trip
	inlines = [Activ_Inline]

	def get_readonly_fields(self, request, obj = None):
		if obj:
			return ['total_expenses']
		return self.readonly_fields


admin.site.register(Trip, Trip_Admin)