import dj_database_url
import os
from pathlib import Path
import sys
from dotenv import load_dotenv
# load_dotenv()  # Load environment variables



# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "apps"))
load_dotenv(dotenv_path=BASE_DIR / '.env')

# Security
SECRET_KEY = os.getenv('SECRET_KEY')  # Replace with a strong secret key

load_dotenv(BASE_DIR / '.env')

DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]


ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host.strip()]



# Installed Apps
INSTALLED_APPS = [
    # 'admin_soft.apps.AdminSoftDashboardConfig',
    # "unfold",  # Add this line (must be above 'django.contrib.admin')
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.branding',
    'apps.contact',
    'apps.skills',
    'apps.work_experience',
    'apps.projects',
    'apps.services',
    'apps.education',
    'apps.github',
    'colorfield',  # GitHub Integration App
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Enables WhiteNoise for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL Configuration
ROOT_URLCONF = 'portfolio.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'branding.context_processors.branding_context',  
            ],
        },
    },
]

# WSGI Application
WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database
USE_POSTGRES = os.environ.get('USE_POSTGRES', 'False') == 'True'


if USE_POSTGRES:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=not DEBUG  # Disable SSL in local dev only
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Source static files during development
STATIC_ROOT = BASE_DIR / "staticfiles"  # Collected static files for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Enable caching and compression

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Print MEDIA_ROOT for debugging
print(f"MEDIA_ROOT is set to: {MEDIA_ROOT}")

# Default Primary Key Field Type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
















# Email Config
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


GEMINI_API_KEYS = [key.strip() for key in os.getenv("GEMINI_API_KEYS", "").split(",") if key.strip()]

ZEROBOUNCE_API_KEY = [key.strip() for key in os.getenv("ZEROBOUNCE_API_KEY", "").split(",") if key.strip()]



# Print to test (you can remove these lines later)
