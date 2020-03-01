from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User

from django.utils.translation import ugettext_lazy as _
try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists,
                                get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.helpers import complete_social_login
    from allauth.socialaccount.models import SocialAccount
    from allauth.socialaccount.providers.base import AuthProcess
except ImportError:
    raise

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','phone','avatar']
        extra_kwargs={'email':{'read_only':True},}

class CustomRegisterSerializer(serializers.Serializer):
    # username = serializers.CharField(
    #     max_length=get_username_max_length(),
    #     min_length=allauth_settings.USERNAME_MIN_LENGTH,
    #     required=True,
    #         help_text='Username must be a unique',
    # )

    first_name = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=True,
            help_text='Your firstname',
    )
    phone = serializers.CharField(
        max_length=14,
        min_length=14,
        required=True,
            help_text='Your phone number must be a unique',
    )
    # phone = serializers.CharField()
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED,
        help_text='Email must be a unique')
    password1 = serializers.CharField(write_only=True,required=True,
        help_text='password',
        style={'input_type': 'password',})
    password2 = serializers.CharField(write_only=True,required=True,
        help_text='confirm password',
        style={'input_type': 'password',})

    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            # 'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user