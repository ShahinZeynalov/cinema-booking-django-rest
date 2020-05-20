from rest_framework import serializers
from .models import *

class MovieFotmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id','title', 'slug', 'age_restriction', 'average', 'formats', 'poster', 'now_playing']

class MovieDetailSerializer(serializers.ModelSerializer):
    formats = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields ='__all__'
    def get_formats(self,obj):
        return MovieFotmatSerializer(obj.formats.all(), many=True).data


# class TheaterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Theater
#         fields='__all__'


class FilteredTheaterSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        print('--------', data.all())
        data = data.all()
        
        return super(FilteredTheaterSerializer, self).to_representation(data)


class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        list_serializer_class = FilteredTheaterSerializer
        model = Theater
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    theaters = TheaterSerializer(many = True)

    class Meta:
        model=City
        fields=['name', 'theaters']


class HallSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()
    class Meta:
        model = Hall
        fields = ['name','theater','seats']


class SessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = '__all__'


class SessionDateSerializer(serializers.ModelSerializer):
    # times  = serializers.SerializerMethodField()
    class Meta:
        model = SessionDate
        fields=['date', 'id']
    # def get_times(self,obj):
    #     return SessionTimeSerializer(obj.times.all(),many=True).data

class SessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    hall = HallSerializer()
    class Meta:
        model = Session
        fields ='__all__'

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
