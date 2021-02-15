import os
from decouple import config
import environ



env = environ.Env(
    # set casting, default value
   # DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    'core'
#From Django-Security Test _________
#    'corsheaders', ----Run an Error 
#    'rest_framework',
 #   'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RollinTestStructure.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'RollinTestStructure.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images) For Development Starts ------

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Static files (CSS, JavaScript, Images) For Development Ends ---------
#---------------------
# Static files (CSS, JavaScript, Images) For Production Starts Online------

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# STATIC_ROOT='/home/rollakft/public_html/static_root'
# MEDIA_ROOT='/home/rollakft/public_html/media_root'

# Static files (CSS, JavaScript, Images) For Production Ends Online---------


# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'
