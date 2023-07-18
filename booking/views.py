from django.shortcuts import render, get_object_or_404 # remove?
from django.views import generic
from .models import Event, Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MakeBookingForm
from django.views.generic.edit import FormView


class EventList(generic.ListView):

    current_event = 'Green Square'
    template_name = 'index.html'
    model = Event


class ViewBookings(LoginRequiredMixin, generic.ListView):

    model = Booking
    template_name = 'mybookings.html'
    queryset = Booking.objects.order_by('-booked_on')


class MakeBooking(LoginRequiredMixin, FormView):

    form_class = MakeBookingForm
    template_name = 'makebooking.html'









