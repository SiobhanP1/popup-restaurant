from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.utils import timezone


NUMBER_OF_GUESTS = ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"))
STATUS = ((1, "Confirmed"), (0, "Waiting list"))


class Event(models.Model):

    event_date = models.DateTimeField(default=timezone.localtime)
    created_on = models.DateTimeField(auto_now_add=True)
    event_name = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name

    def get_default_event():
        return Event.objects.get_or_create(name="default")[0]


class Booking(models.Model):

    guest = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="bookings")
    booked_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    num_of_guests = models.IntegerField(choices=NUMBER_OF_GUESTS, default=1)
    booking_status = models.IntegerField(choices=STATUS, default=1)
    event = "Green Square Gardens"

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return f"{self.guest} booked {self.event.event_name}"

    def get_absolute_url(self):
        return reverse('bookings')
