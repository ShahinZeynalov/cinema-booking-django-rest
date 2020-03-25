from django.urls import path,include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'comments', CommentViewSet)

app_name='api'
urlpatterns = [
    path('sessions/', SessionListAPIView.as_view()),
    path('sessions/<pk>', SessionRetriveAPIView.as_view(),name='session'),
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<abc>', MovieDetailAPIView.as_view(),name='movie'),
    path('booking/', BookingCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('cities/', CityListAPIView.as_view(), name='cities')

]
