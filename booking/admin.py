from django.contrib import admin
from .models import Booking, Event


admin.site.register(Booking)
admin.site.register(Event)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('event', 'booked_on', 'guest', 'num_of_guests', 'status')
    list_filter = ['status', 'event']


class EventAdmin(admin.ModelAdmin):

    list_display = ('event_name', 'created_on', 'event_date')
    list_filter = ['event_name']