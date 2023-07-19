from django import forms
from django.forms import ModelForm
from .models import Booking

class MakeBookingForm(forms.ModelForm):

    number_of_guests = forms.IntegerField(min_value=1, max_value=4)

    class Meta:
        model = Booking
        fields = ['number_of_guests']