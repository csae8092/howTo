from .base import *

SECRET_KEY = '!i%7s@1+v&asdf*kljxcvghjtt5=dxxaeee-3dtms()pw^et!we'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
