from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Session,Booking,Comment
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class=MovieSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
    lookup_url_kwarg='abc'




class SessionListAPIView(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    filter_backends =(DjangoFilterBackend,)
    filter_fields=('hall__theater__city','hall__theater')




class SessionRetriveAPIView(generics.RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionDetailSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
    def perform_update(self,serializer):
        serializer.save(user = self.request.user)



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =(IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
    def perform_update(self,serializer):
        serializer.save(user = self.request.user)
