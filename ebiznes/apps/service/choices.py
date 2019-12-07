from django.utils.translation import ugettext_lazy as _


WAITING = 'WAITING_FOR_APPROVAL'
APPROVED = 'APPROVED'
DONE = 'DONE'
NOT_APPROVED = 'NOT_APPROVED'

STATUS_CHOICES = (
    (WAITING, _('Waiting for approval')),
    (NOT_APPROVED, _('Not approved')),
    (APPROVED, _('Approved')),
    (DONE, _('Done')),
)

PENDING = 'PENDING'
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'

PAYMENT_CHOICES = (
    (PENDING, 'W trakcie'),
    (SUCCESS, 'Udane'),
    (FAILURE, 'Nie udane'),
)
