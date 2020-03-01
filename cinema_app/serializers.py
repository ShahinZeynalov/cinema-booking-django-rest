
from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['title','slug','age_restriction','average','format','poster']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['name']

class TheaterSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Theater
        fields=['name','city']

class HallSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()
    class Meta:
        model = Hall
        fields=['name','theater','seats']

class SessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = '__all__'
class  SessionDateSerializer(serializers.ModelSerializer):
    times  = serializers.SerializerMethodField()

    class Meta:
        model = SessionDate
        fields='__all__'

    def get_times(self,obj):
        return SessionTimeSerializer(obj.times.all(),many=True).data



class SessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Session
        fields =['id', 'movie']


class SessionDetailSerializer(serializers.ModelSerializer):

    hall=HallSerializer()
    dates = serializers.SerializerMethodField()
    # movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True)
    movie = MovieSerializer()

    class Meta:
        model = Session
        fields ='__all__'

    def get_dates(self, obj):
        return SessionDateSerializer(obj.dates.all(), many=True).data





class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields='__all__'
class BookingSerializer(serializers.ModelSerializer):
    # seats = serializers.SerializerMethodField()

    # seats = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='booking-detail'
    # )
    class Meta:
        model = Booking
        read_only_fields=('user','ticket_id')
        fields = ['datetime','session','seats','ticket_id']
        # fields='__all__'
    # def get_seats(self, obj):
    #     return SeatSerializer(obj.seats.all(), many=True).data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields=('user',)
        fields='__all__'