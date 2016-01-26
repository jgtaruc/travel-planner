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


admin.site.register(Trip, Trip_Admin)