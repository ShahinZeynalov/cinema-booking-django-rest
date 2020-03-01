from django.contrib import admin

from .models import *


admin.site.register([
    Booking,
    Hour,
    Movie,
    Session,
    Seat,
    Hall,
    City,
    Theater,
    MovieFormat,
    Genre,
    SessionDate,
    HallType,
    Comment
])
