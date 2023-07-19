from django.db import models
from django.contrib.auth.models import User


NUMBER_OF_GUESTS = ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"))
STATUS = ((1, "Confirmed"), (0, "Waiting list"))


class Booking(models.Model):

    guest = models.ForeignKey( User, on_delete = models.CASCADE, related_name = "bookings")
    booked_on = models.DateTimeField(auto_now_add = True)
    last_edited = models.DateTimeField(auto_now = True)
    num_of_guests = models.IntegerField(choices=NUMBER_OF_GUESTS, default=1)
    booking_status = models.IntegerField(choices=STATUS, default=1)
    event = "Green Gardens"
    event_date = "August 30th, 7-9pm"
    #event = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return self.event


class Event(models.Model):

    event_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name