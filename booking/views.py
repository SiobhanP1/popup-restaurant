from django.shortcuts import render, get_object_or_404 # remove?
from django.views import View, generic
from .models import Event, Booking
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import MakeBookingForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy


class EventList(generic.ListView):

    current_event = 'Green Square'
    template_name = 'index.html'
    model = Event


class ViewBookings(LoginRequiredMixin, generic.ListView):

    model = Booking
    template_name = 'mybookings.html'
    queryset = Booking.objects.order_by('-booked_on')
    paginate_by = 5


class MakeBooking(LoginRequiredMixin, CreateView):

    model = Booking
    fields = ['num_of_guests']
    template_name = 'makebooking.html'
    success_url = reverse_lazy("my_bookings")

    def form_valid(self, form):
        form.instance.guest = self.request.user
        messages.success(self.request, "Successfully booked.")
        return super(MakeBooking, self).form_valid(form)
    

class ThankYou(LoginRequiredMixin, View):

    template_name = 'thankyou.html'







