from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import CommondBase


class User(AbstractUser):
    pass