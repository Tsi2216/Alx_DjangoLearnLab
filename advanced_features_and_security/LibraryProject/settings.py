"""
Django settings for LibraryProject project.
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='django-insecure-g4q8c=)!=5s&k)chf#z3!xqedd6vc!)=#rzm@)!3gm0#l0nf4i')

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG to False in production for security.
DEBUG = config('DJANGO_DEBUG', default='False') == 'True'

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your apps here
    'relationship_app',
    'bookshelf',
]

# Middleware order is important for security. SecurityMiddleware should be at the top.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Handles secure redirects and headers
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Handles X_FRAME_OPTIONS
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# --- Security Enhancements ---
# Step 1: Secure Settings
# 
# 1. Enforce HTTPS.
# Redirects all HTTP requests to HTTPS. Requires a properly configured SSL/TLS certificate.
SECURE_SSL_REDIRECT = True
# HSTS tells browsers to only access the site via HTTPS for a specified time.
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 2. Enforce Secure Cookies.
# Ensures session cookies are only transmitted over HTTPS.
SESSION_COOKIE_SECURE = True
# Ensures CSRF cookies are only transmitted over HTTPS.
CSRF_COOKIE_SECURE = True

# 3. Implement Secure Headers.
# Prevents the site from being framed, protecting against clickjacking attacks.
X_FRAME_OPTIONS = 'DENY'
# Prevents browsers from MIME-sniffing and helps mitigate certain XSS attacks.
SECURE_CONTENT_TYPE_NOSNIFF = True
# Enables the browser’s built-in XSS filtering.
SECURE_BROWSER_XSS_FILTER = True

# Step 4: Implement Content Security Policy (CSP)
# A strong CSP helps prevent a wide range of attacks, including XSS.
# You typically use a separate package like `django-csp`.
# Uncomment the following lines after installing `django-csp` (`pip install django-csp`).
# MIDDLEWARE.insert(0, 'csp.middleware.CSPMiddleware')
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_IMG_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com")