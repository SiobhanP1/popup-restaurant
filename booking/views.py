from django.shortcuts import render, get_object_or_404 # remove?
from django.views import generic
from .models import Event


class EventList(generic.ListView):

    current_event = 'Green Square'
    template_name = 'index.html'
    model = Event





