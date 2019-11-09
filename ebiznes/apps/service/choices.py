from django.utils.translation import gettext as _


WAITING = 'Waiting for approval'
APPROVED = 'Approved'
DONE = 'Done'
NOT_APPROVED = 'Not approved'

STATUS_CHOICES = (
    (WAITING, _(WAITING)),
    (NOT_APPROVED, _(NOT_APPROVED)),
    (APPROVED, _(APPROVED)),
    (DONE, _(DONE)),
)
