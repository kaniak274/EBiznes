from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from model_utils.models import TimeStampedModel


class Profession(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    owner = models.ForeignKey(get_user_model(), related_name='services', on_delete=models.CASCADE)

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    city = models.CharField(_('City'), max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, blank=True, null=True)
    service_logo = models.ImageField(_('Service logo'), upload_to="logos/", max_length=255, null=True, blank=True)
    street = models.CharField(_('Street'), max_length=255, blank=True, null=True)
    phone_number = models.CharField(_('Phone number'), max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def rate(self):
        ### TODO: ADD RATING CALCULATION HERE
        return 2.5


class Rating(models.Model):
    rating = models.DecimalField(_('Rating'), max_digits=3, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('5.00'))])

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='ratings')

    comment = models.TextField(_('Comment'), null=True, blank=True)

    class Meta:
        unique_together = ('owner', 'service')

