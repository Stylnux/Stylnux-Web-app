"""
Django settings for ecom_app project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
import dj_database_url
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

from decouple import config
from django.core.management.utils import get_random_secret_key


# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key(), cast=str)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'render.apps.RenderConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "djoser",
    "rest_framework",
    # 'rest_framework.authtoken',
    #includedpapps
    "users",
    # "products",
    "likes",
    "tags",
    "store",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecom_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecom_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# DATABASES = {
#     'default': dj_database_url.config(        # Feel free to alter this value to suit your needs.
#     default='postgresql://postgres:postgres@localhost:5432/mysite',
#     conn_max_age=600    )}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront2',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'MyPassword'
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTH_USER_MODEL = 'users.User'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'users.serializers.UserCreateSerializer',
        'current_user': 'users.serializers.UserSerializer',
        # 'user_delete': 'djoser.serializers.UsersDelete.'
    }
}
# DJOSER = {
#     'LOGIN_FIELD': 'email',
#     'USER_CREATE_PASSWORD_RETYPE': True,
#     'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
#     'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
#     'SEND_CONFIRMATION_EMAIL': True,
#     'SET_USERNAME_RETYPE': True,
#     'SET_PASSWORD_RETYPE': True,
#     'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL': 'activate/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL': True,
#     'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
#     'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
#     'SERIALIZERS': {
#         'user_create': 'accounts.serializers.UserCreateSerializer',
#         'user': 'accounts.serializers.UserCreateSerializer',
#         'current_user': 'accounts.serializers.UserCreateSerializer',
#         'user_delete': 'djoser.serializers.UserDeleteSerializer',
#     }
# }

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '[YOUR GOOGLE OAUTH2 API KEY]'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '[YOUR GOOGLE OAUTH2 API SECRET]'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']
# SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

# SOCIAL_AUTH_FACEBOOK_KEY = '[YOUR FACEBOOK API KEY]'
# SOCIAL_AUTH_FACEBOOK_SECRET = '[YOUR FACEBOOK API SECRET]'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields': 'email, first_name, last_name'
# }

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1)
}


# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="dummy@email.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="dummy123")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False