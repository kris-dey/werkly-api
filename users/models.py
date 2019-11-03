
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    USER_TYPE = (
    	('W', 'Worker'),
    	('E', 'Employer')
    )
    user_type = models.CharField(max_length=8, choices=USER_TYPE, default="W")
    wants_to_receive_marketing_emails = models.BooleanField(default=False)
    def __str__(self):
        return self.email
