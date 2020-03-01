from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    # phone = models.CharField(max_length=20,null=True,blank=True,unique=True)
    phone = PhoneNumberField()
    birthday = models.DateField(null=True,blank=True)
    card_number = models.CharField(max_length=55,null=True,blank=True)
    email = models.EmailField(max_length=55,unique=True)
    avatar = models.ImageField(null=True,blank = True)
