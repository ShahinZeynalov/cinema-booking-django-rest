from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from .models import  Session

@receiver(post_save, sender = Session)
def change_now_showing(instance, created, **kwargs):
    if created:
        instance.movie.now_playing = True
        instance.movie.save()
