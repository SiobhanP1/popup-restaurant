from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('login/mybookings/', views.ViewBookings.as_view(), name='my_bookings')
]