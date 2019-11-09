from django.utils.translation import gettext as _


WAITING = 'Waiting for approval'
APPROVED = 'Approved'
DONE = 'Done'

STATUS_CHOICES = (
    (WAITING, _(WAITING)),
    (APPROVED, _(APPROVED)),
    (DONE, _(DONE)),
)
