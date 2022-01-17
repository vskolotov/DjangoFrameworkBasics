from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


def default_key_expiration_date():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64,
                            verbose_name='город',
                            blank=True)
    phone_number = models.CharField(max_length=14,
                                    verbose_name='номер телефона',
                                    blank=True)
    avatar = models.ImageField(upload_to='users_avatars',
                               blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст',
                                      blank=True,
                                      null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=default_key_expiration_date)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
