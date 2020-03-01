from django.urls import path,include
from django.conf.urls import url

from .views import *
app_name='api'
urlpatterns = [
    path('sessions/',SessionListAPIView.as_view()),
    path('sessions/<pk>',SessionRetriveAPIView.as_view(),name='sessions'),
    path('movies/',MovieListAPIView.as_view()),
    path('movies/<abc>',MovieDetailAPIView.as_view()),
    path('booking/',BookingCreateAPIView.as_view()),


]
