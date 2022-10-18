from .base import *

DEBUG=True

ALLOWED_HOSTS = ["*"]

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env('DATABASE_NAME'),
#         'USER':env('DATABASE_USER'),
#         'PASSWORD':env('DATABASE_PASSWORD'),
#         'HOST':env('DATABASE_HOST'),
#         'PORT':'5432',
#     }
# }