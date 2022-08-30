from .base import *

DEBUG=False

ALLOWED_HOSTS = ["www.mertemirkaya.com","mertemirkaya.com","46.101.237.57"]

STATIC_ROOT=os.path.join(BASE_DIR,'static/')

AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE=False
AWS_S3_REGION_NAME =env('AWS_S3_REGION_NAME')
AWS_S3_SIGNATURE_VERSION ="s3v4"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER':env('DATABASE_USER'),
        'PASSWORD':env('DATABASE_PASSWORD'),
        'HOST':env('DATABASE_HOST'),
        'PORT':'',
    }
}