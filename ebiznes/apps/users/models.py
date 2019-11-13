from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    phone_number = models.CharField(_('Phone number'), max_length=30, null=True, blank=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)

