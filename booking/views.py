from django.shortcuts import render, get_object_or_404 # remove?
from django.views import generic
from .models import Event, Booking
from django.contrib.auth.mixins import LoginRequiredMixin


class EventList(generic.ListView):

    current_event = 'Green Square'
    template_name = 'index.html'
    model = Event


class ViewBookings(LoginRequiredMixin, generic.ListView):

    model = Booking
    template_name = 'viewbookings.html'
    queryset = Booking.objects.order_by('-booked_on')






