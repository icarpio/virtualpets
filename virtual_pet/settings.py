
from pathlib import Path
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
REDIS_URL = os.environ.get('REDIS_URL')
DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pets',
    'accounts'
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

ROOT_URLCONF = 'virtual_pet.urls'

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

WSGI_APPLICATION = 'virtual_pet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),      
        'USER': os.getenv('DB_USER'),      
        'PASSWORD': os.getenv('DB_PASSWORD'), 
        'HOST': os.getenv('DB_HOST'),      
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'options': '-c search_path=virtualpets',  # Usar un esquema diferente por cada app
        },
    }
}

CELERY_BROKER_URL =  REDIS_URL  
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = REDIS_URL 

LOGIN_URL = 'login'  # Ruta para redirigir al login si no está autenticado
LOGIN_REDIRECT_URL = 'pet_dashboard'  # Redirección tras el login
LOGOUT_REDIRECT_URL = 'login'  # Redirección tras el logout


SESSION_COOKIE_NAME = 'virtualpet_sessionid'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
# En desarrollo, cuando DEBUG es True
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'pets', 'static')]
else:
    # En producción, cuando DEBUG es False
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Carpeta estática raíz
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

