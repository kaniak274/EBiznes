from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _

from model_utils.models import TimeStampedModel

from .choices import *
from .utils import send_email


class Profession(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('profession')
        verbose_name_plural = _('professions')

    def __str__(self):
        return self.name


digits_only = RegexValidator(r'^[0-9]*$', _('Only digits are allowed.'))


class Service(TimeStampedModel):
    owner = models.ForeignKey(get_user_model(), related_name='services',
        on_delete=models.CASCADE, verbose_name=_('Owner'))

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    city = models.CharField(_('City'), max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name=_('Profession'))
    service_logo = models.ImageField(_('Service logo'), upload_to="logos/", max_length=255, null=True, blank=True)
    street = models.CharField(_('Street'), max_length=255, blank=True, null=True)
    phone_number = models.CharField(_('Phone number'), max_length=30, blank=True, null=True)
    account_number = models.CharField(_('Account number'), max_length=26,
        null=True, blank=True, validators=[digits_only])

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.name

    @property
    def random_ratings(self):
        return self.ratings.all().order_by('?')[:5]

    @property
    def rate(self):
        ratings = self.ratings.all()
        if ratings:
            ratings_sum = sum([float(r.rating) for r in ratings])
            result = ratings_sum / ratings.count()
        else:
            result = 0
        return result

class Rating(TimeStampedModel):
    rating = models.DecimalField(_('Rating'), max_digits=3, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('5.00'))])

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='ratings',
        verbose_name=_('Owner'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='ratings',
        verbose_name=_('Service'))

    comment = models.TextField(_('Comment'), null=True, blank=True)

    def __str__(self):
        return 'Rating {} - {}'.format(self.service.name, self.owner.username)

    class Meta:
        unique_together = ('owner', 'service')
        verbose_name = _('rating')
        verbose_name_plural = _('ratings')


class Rent(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='rents',
        verbose_name=_('User'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='rents',
        verbose_name=_('Service'))

    status = models.CharField(max_length=100, default=WAITING, choices=STATUS_CHOICES,
        verbose_name=_('Status'))
    phone_number = models.CharField(_('Phone number'), max_length=20, null=True, blank=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)
    total_price = models.DecimalField(_('Total price'), max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(_('Paid'), default=False)

    class Meta:
        verbose_name = _('rent')
        verbose_name_plural = _('rents')

    def save(self, *args, **kwargs):
        if self.status == APPROVED or self.status == NOT_APPROVED:
            if self.status == APPROVED:
                msg_ctx = {
                    'name': self.service.name,
                    'approved': True
                }
            else:
                msg_ctx = {
                    'name': self.service.name,
                    'approved': False
                }

            send_email(
                'ServiceRent approval',
                'service/email/approval.html',
                [self.user.email],
                msg_ctx,
            )
        elif self.status == DONE and not self.is_paid:
            msg_ctx = {
                'pk': self.pk
            }

            send_email(
                'Zaplata za usluge',
                'service/email/payment.html',
                [self.user.email],
                msg_ctx,
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return 'Rent {} - {}'.format(self.service.name, self.user.username)


class PriceList(models.Model):
    service = models.ForeignKey(Service,
        verbose_name=_("Service"), on_delete=models.CASCADE, related_name="price_list")

    name = models.CharField(_("Name"), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=6, decimal_places=2)

    @classmethod
    def calculate_total_price(cls, price_list):
        return cls.objects.filter(pk__in=price_list).aggregate(Sum('price'))

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    totalAmount = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    status = models.CharField(max_length=40, choices=PAYMENT_CHOICES)
