"""
Django settings for mymindwiki project.

"""

import logging
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
import environ

env = environ.Env(
    #
    ALLOWED_HOSTS=(list, []),
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG=(bool, False),
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY=(str, 'DEV-ENV-ONLY'),
    #
    SITE_HOSTNAME=(str, 'localhost'),
    #
    SITE_PORT=(int, 1312),
    #
    SSL_ENABLED=(bool, False),
)

logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
# environ.Env.read_env()

try:
    DATA_DIR = Path(env("DATA_DIR"))
    DATABASE_DIR = DATA_DIR / "db"
    MEDIA_ROOT = DATA_DIR / "media"
    STATIC_ROOT = DATA_DIR / "static"
except Exception as e:
    logger.debug(
        "Environment variable 'DATA_DIR' not set, looking for 'DATABASE_DIR' "
        "and 'MEDIA_DIR' instead.")
    DATABASE_DIR = Path(env("DATABASE_DIR"))
    MEDIA_ROOT = Path(env("MEDIA_DIR"))
    STATIC_ROOT = Path(env("STATIC_DIR"))

DEBUG = env('DEBUG')
SECRET_KEY = env("SECRET_KEY")

if DEBUG is False and SECRET_KEY == 'DEV-ENV-ONLY':
    logger.critical(
        "Environment variable 'SECRET_KEY' must be set if 'DEBUG' is False")
    raise ImproperlyConfigured

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

SITE_HOSTNAME = env('SITE_HOSTNAME')
SITE_PORT = env('SITE_PORT')
SSL_ENABLED = env('SSL_ENABLED')

XPORT = 'http://'
if SSL_ENABLED:
    XPORT = 'https://'
EXTERNAL_URL = f"{XPORT}{SITE_HOSTNAME}:{SITE_PORT}"

# Application definition

INSTALLED_APPS = [
    'mindwiki.apps.MindWikiConfig',
    'word_cloud.apps.WordCloudConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mymindwiki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "mymindwiki" / 'templates',
        ],
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

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'codehilite',
    'fenced_code',
    'tables',
    'toc',
    'wikilinks',
    'mindwiki.markdown_ext.ext_links',
    'mindwiki.markdown_ext.snippets',
]
MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {
    'wikilinks': {
        'base_url': '/wiki/page/'
    },
    'mindwiki.markdown_ext.ext_links': {
        'base_url': EXTERNAL_URL + '/wiki/weblink/',
        'end_url': '/?json=true',
    },
    'mindwiki.markdown_ext.snippets': {
        'base_url': EXTERNAL_URL + '/wiki/snippet/',
        'end_url': '/?json=true',
    },
}

WSGI_APPLICATION = 'mymindwiki.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "mymindwiki" / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'


