from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = [
    'kaniak274.service-rent.pl',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'local')
]

WEBPACK_MANIFEST_FILE = os.path.join(BASE_DIR, '../manifest-dist.json')
