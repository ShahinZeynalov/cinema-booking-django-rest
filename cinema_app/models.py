from django.db import models
from account_app.models import User
import uuid
import datetime
from django.template.defaultfilters import slugify

def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1].upper()

class MovieFormat(models.Model):
    name=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Genre(models.Model):
    name = models.CharField(max_length=23)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(max_length=500)
    runtime = models.CharField(max_length=20)
    director = models.CharField(max_length=20,default='Anonim')
    average = models.CharField(max_length=3)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE)
    production_company = models.CharField(max_length=55)
    release_date = models.DateField()
    casts = models.CharField(max_length=127)
    poster= models.ImageField(upload_to='movie_posters/')
    now_playing = models.BooleanField(default=False,blank=True)
    trailer = models.URLField()
    lang = models.CharField(max_length = 7)
    formats = models.ManyToManyField('MovieFormat')
    slug = models.SlugField(null=True,blank=True)
    age_restriction = models.CharField(max_length=2, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'Title:{self.title} Lang:{ self.lang}'

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

class Hour(models.Model):
        hour = models.TimeField()
        def __str__(self):
            return f'{self.hour}'

class SessionDate(models.Model):
    date = models.DateField()
    times = models.ManyToManyField('Hour')

    def __str__(self):
        return f' {self.date}'

class City(models.Model):
    name = models.CharField(max_length=31)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Theater(models.Model):
    name = models.CharField(max_length=31)
    city = models.ForeignKey('City',on_delete=models.CASCADE, related_name='theaters')
    address = models.CharField(max_length = 127)
    phone = models.CharField(max_length=15,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Theater, self).save(*args, **kwargs)
class HallType(models.Model):
    price = models.DecimalField(max_digits=3,decimal_places=1,default=0.0)
    image = models.ImageField(null=True,blank=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.type}'

class Hall(models.Model):
    name = models.CharField(max_length=31)
    seats = models.ManyToManyField('Seat')
    theater = models.ForeignKey('Theater',on_delete=models.CASCADE,related_name='halls')
    type = models.ForeignKey('HallType',on_delete=models.CASCADE)

    type = models.ForeignKey('HallType',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'{self.theater.city} {self.theater} {self.name} '

class Seat(models.Model):
    row = models.PositiveSmallIntegerField(default=0)
    column = models.PositiveSmallIntegerField(default=0)
    number = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'id:{self.id} is active: {self.active} row: {self.row} column: {self.column} seat: {self.number}'
class Session(models.Model):
    movie = models.ForeignKey('Movie',on_delete=models.CASCADE)
    dates = models.ManyToManyField('SessionDate')
    hall = models.ForeignKey('Hall',on_delete=models.CASCADE, related_name='sessions')
    slug = models.SlugField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'{ self.movie} {self.hall}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.movie.title)
        super(Session, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie} {self.reply} {self.created_at}'


CANCELED, TENTATIVE, CONFIRMED, BOOKED = range(-1, 3)
STATUS = (
    (CANCELED, "Canceled"),
    (TENTATIVE, "Tentative booked"),
    (CONFIRMED, "Confirmed"),
    (BOOKED, "Booked")
)

class ActiveReservationsManager(models.Manager):
    def get_queryset(self):
        """Returns either CONFIRMED, BOOKED reservations or TENTATIVE but not older than 2 min"""
        time_limit = datetime.datetime.now() -  datetime.timedelta(seconds=settings.TENTATIVE_BOOKED_SEC)
        return super(ActiveReservationsManager, self).get_queryset().exclude(
            status=CANCELED).filter(
            (Q(reservation_start__gte=time_limit) & Q(status__gte=TENTATIVE)) | Q(status__gte=CONFIRMED))


class Booking(models.Model):
    """Create Reservation"""
    seats = models.ManyToManyField(Seat,related_name='seat')
    session = models.ForeignKey('Session',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    datetime = models.DateTimeField()
    ticket_id = models.CharField(max_length=127,blank=True,null=True)
    objects = models.Manager()
    active_reservations = ActiveReservationsManager()
    amount = models.DecimalField(max_digits=5, decimal_places=2,
                                 null=True, blank=True)

    reservation_start = models.DateTimeField(auto_now_add=True)
    reservation_confirmed = models.DateTimeField(blank=True, null=True)


    def save(self, *args, **kwargs):
        # print('------------------------',self.ticket_id)
        # if len(self.ticket_id.strip(" "))==0:
        self.ticket_id = generate_ticket_id()
            # print('-------------------',generate_ticket_id())

        super(Booking, self).save(*args, **kwargs)


    def __str__(self):
        return  f'{self.user.username} {self.datetime} '
