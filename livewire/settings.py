"""
Django settings for livewire project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j4s_1z9bread6!n2ck7scf!d4eggs^at$vs9g^of04%rdkwc#v+e%muga8*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['livewire-webdev.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'about.apps.AboutConfig',
    'work.apps.WorkConfig',
    'jobs.apps.JobsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'livewire.urls'

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

WSGI_APPLICATION = 'livewire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'da6hournl39ac6',
        'USER':'xbzcsjcewqdejv',
        'PASSWORD':'b0bcfd16dffce49f8296976038abdc000e522a54be340572a41b41395d6d9e5b',
        'HOST':'ec2-174-129-225-9.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'livewiredb',
#        'USER':'postgres',
#        'PASSWORD':'ninonina44',
#        'HOST':'localhost',
#        'PORT':'5432',
#    }
#}
#postgres://xbzcsjcewqdejv:b0bcfd16dffce49f8296976038abdc000e522a54be340572a41b41395d6d9e5b@ec2-174-129-225-9.compute-1.amazonaws.com:5432/da6hournl39ac6

#postgres://kqbbeocgaznqht:834f6d1557e067f35768e7139fc8822b92354ebb4ad915d2ccd99638e3a57619@ec2-174-129-206-173.compute-1.amazonaws.com:5432/d4l4escrnnm08v
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators


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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'livewire/static/')
]

#STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

#AWS_STORAGE_BUCKET_NAME = 'livewire-project'
#AWS_S3_REGION_NAME = 'eu-west-2'  # e.g. us-east-2
#AWS_ACCESS_KEY_ID = 'AKIAJYVWYO4J4RJK5GQA'
#AWS_SECRET_ACCESS_KEY = 'JS+QTkQaTMdRtWVaSomXANfh3mKtGVOPVe3NBUt6'

# Tell django-storages the domain to use to refer to static files.
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_LOCATION = 'static'
#STATICFILES_STORAGE = 'custom_storages.StaticStorage'

#MEDIAFILES_LOCATION = 'media'
#DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
