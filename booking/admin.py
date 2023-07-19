from django.contrib import admin
from .models import Booking


admin.site.register(Booking)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('event', 'booked_on', 'guest', 'num_of_guests', 'status')
    list_filter = ['status', 'event']


class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on')