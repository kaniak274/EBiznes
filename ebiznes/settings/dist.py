from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = [
    'service-rent.kaniak274.usermd.net',
    'localhost',
]

WEBPACK_MANIFEST_FILE = os.path.join(BASE_DIR, '../manifest-dist.json')

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static', 'local')
#]

ENV_PATH = os.path.abspath(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(ENV_PATH, '../../public/static/')
MEDIA_ROOT = os.path.join(ENV_PATH, '../../public/media/')

STATICFILES_DIRS = [
    os.path.join(ENV_PATH, '../static', 'dist')
]
