from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class Profile(AbstractUser):
    description = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=9, \
        validators=[RegexValidator(regex="^\\d{9}$", message="Invalid phone number format")])

    def __str__(self):
        return self.username


