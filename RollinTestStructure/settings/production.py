from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['127.0.0.1']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


DATABASES = {
    'default': {
# Database (Mysql) For Test on Local Device Starts -------
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# Database (Mysql) For Test on Local Device Ends-------     

# Database (Mysql) For Productions Starts-------      
#For Test Purpose -------------
    #Instruction- Fill Up Database Environment Variables Below...
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': '',
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
    }
}
# Database (Mysql) For Productions Starts-------    

# Static files (CSS, JavaScript, Images) For Production

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# STATIC_ROOT='/home/rollakft/public_html/static_root'
# MEDIA_ROOT='/home/rollakft/public_html/media_root'

# Static files (CSS, JavaScript, Images) For Production ----For Testing on local Device------ #
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
# Static files (CSS, JavaScript, Images) For Production ----For Testing on local Device------ #
