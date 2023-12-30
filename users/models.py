from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    value = models.PositiveIntegerField(default=0)
    coin = models.PositiveIntegerField(default=0)