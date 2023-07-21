from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('login/bookings/', views.ViewBookings.as_view(), name='bookings'),
    path('login/makebooking/', views.MakeBooking.as_view(),
         name='make_booking'),
    path('login/bookings/editbooking/<int:pk>/', views.EditBooking.as_view(),
         name='edit_booking'),
    path('login/bookings/cancelbooking/<int:pk>/',
         views.CancelBooking.as_view(), name='cancel_booking'),
]
