from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

class MyUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    email_name = models.EmailField(unique=True, max_length=150)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(null=True, blank=True)


