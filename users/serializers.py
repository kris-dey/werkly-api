from rest_framework import serializers
from . import models
from rest_auth.models import TokenModel
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.core.validators import RegexValidator
from django.http import HttpResponse

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('id','email','username','first_name','last_name','phone_number', 'user_type','wants_to_receive_marketing_emails')

class TokenSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = TokenModel
		fields = ('key', 'user')

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('id','email','username','first_name','last_name','phone_number', 'user_type','wants_to_receive_marketing_emails')

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    USER_TYPE = (
		('W', 'Worker'),
		('E', 'Employer')
	)
    user_type = serializers.ChoiceField(choices=USER_TYPE)
    phone_number = serializers.CharField(max_length=17) # validators should be a list
    wants_to_receive_marketing_emails = serializers.BooleanField(default=False)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username':self.validated_data.get('username','',),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'user_type':self.validated_data.get('user_type',''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone_number':self.validated_data.get('phone_number',''),
            'wants_to_receive_marketing_emails':self.validated_data.get('wants_to_receive_marketing_emails',''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.first_name = self.cleaned_data.get('first_name')
        user.second_name = self.cleaned_data.get('second_name')
        user.email = self.cleaned_data.get('email')
        user.user_type = self.cleaned_data.get('user_type')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.wants_to_receive_marketing_emails = self.cleaned_data.get('wants_to_receive_marketing_emails')
        user.save()
        return user
