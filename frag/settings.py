import os
import shutil
from datetime import timedelta
import sys

import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '52)xj$^6n7pecq6vrp(tx*wp!l6(^opya)1+9)ltz&jc8s@r_4'
DEBUG = True
ALLOWED_HOSTS = []
TIME_ZONE = 'UTC'

INSTALLED_APPS = [
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'obj_ev',
    'users',
    'stats',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'rest_framework_json_api',
    'rest_framework_jwt',
    'corsheaders',
'django_cleanup.apps.CleanupConfig',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
APPEND_SLASH = False
ROOT_URLCONF = 'frag.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'frag.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# For dev
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'obj_db',
#        'USER':'skripnik',
#        'PASSWORD':'Volk_2005',
#        'HOST':'127.0.0.1',
#        'PORT':5432,
#        'TEST': {
#            'NAME': 'test_obj',
#        },
#    }
# }
# For docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'123456',
        'HOST':'engee_db',
        'PORT':5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'


USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = ''
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
AUTH_USER_MODEL = 'users.Userc'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': None,
        'language': 'uk',
    },
}
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
    'DATETIME_FORMAT': "%Y.%m.%d %H:%M",

}

DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'TOKEN_MODEL':None,
    'ACTIVATION_URL': 'activate/{uid}/{token}/',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SERIALIZERS': {'current_user': 'users.serializers.UserProfileSerializer',
                    'user_create': 'users.serializers.UserCreateSerializer',
                    },
}
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=0.5),
    'ROTATE_REFRESH_TOKENS': True,

}
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000",
    "http://192.168.1.177:8000",
    "http://localhost:8080",
    "http://localhost:8081",


]
ALLOWED_HOSTS = ["localhost","127.0.0.1","192.168.1.10","192.168.0.106"]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'mich.sk.freelance@gmail.com'
DEFAULT_FROM_EMAIL = "noreply@engee.com"
EMAIL_HOST_PASSWORD = '1KwdHC3pVFZGsh48'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
if 'test' in sys.argv:
   CACHE_MIDDLEWARE_SECONDS = 0
django_heroku.settings(locals())
AWS_ACCESS_KEY_ID = "AKIAQ3KTD3JP2CHKBLP6"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "hiker-bucket-assets"
# AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = "us-east-1"
AWS_S3_FILE_OVERWRITE = False
AWS_S3_VERIFY = True
# AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'