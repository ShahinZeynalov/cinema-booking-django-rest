from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager

# class UserProfileManager(BaseUserManager):
#     """Helps Django work with our custom model."""
#     def create_user(self,email,first_name,last_name,password):
#         """Create a new user profileobject."""
#         if not email:
#             raise ValueError('User must have an email address.')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email,first_name=first_name,last_name=last_name,password=password)
#         user.self



class User(AbstractUser):
    # phone = models.CharField(max_length=20,null=True,blank=True,unique=True)
    phone = PhoneNumberField()
    birthday = models.DateField(null=True,blank=True)
    card_number = models.CharField(max_length=55,null=True,blank=True)
    email = models.EmailField(max_length=55,unique=True)
    avatar = models.ImageField(null=True,blank = True)
