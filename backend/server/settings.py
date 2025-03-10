"""
Django settings for server project.
"""

from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=False)

# Allowed Hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Disable the trailing slash
APPEND_SLASH = False

# Application definition
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Third-Party Apps Configuration
INSTALLED_APPS += [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
]

# Your Apps Configuration.
INSTALLED_APPS += [
    "user_account.apps.UserAccountConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # If Globely Disable CSRF Protection to comment it
    "user_account.middleware.DisableCSRFMiddleware",  # Disable CSRF Protection for API Requests
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # If you can use socialaccount provider like (google, github, etc.) then use it.
                # "allauth.account.context_processors.account",
                # "allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]

# WSGI_APPLICATION = "server.wsgi.application"
ASGI_APPLICATION = "server.asgi.application"

# Define the Custom User Model
# AUTH_USER_MODEL = "app_name.custom_model_name"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Database Database Configuration
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# PostgreSQL Database Configuration
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# URL prefix for static files
STATIC_URL = "/static/"

# Directory where collectstatic will collect static files for deployment
STATIC_ROOT = BASE_DIR / "staticfiles"

# Additional locations to look for static files
STATICFILES_DIRS = [BASE_DIR / "static"]

# Directory where uploaded files will be stored
MEDIA_ROOT = BASE_DIR / "uploads"

# URL prefix for media files
MEDIA_URL = "/media/"

# Django Rest Framework Configuration
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day",  # 100 requests per day for anonymous users
        "user": "1000/day",  # 1000 requests per day for authenticated users
    },
    "DEFAULT_RENDERER_CLASSES": [
        # Default renderer
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        # Setting the JSONRenderer
        "rest_framework.renderers.JSONRenderer",
    ],
}

# Allowing Origins CORS Request

# Allow all origins (not recommended for production)
CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS", cast=bool, default=False)

# Alternatively, specify allowed origins (Take a list of Origins)
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())

# Simple JWT Configuration
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # Default value is minutes=5
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # Default value is days=1
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),  # Default value is minutes=5
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),  # Default value is days=1
}

# User Authentication Configuration
SITE_ID = 1

# Authentication Configuration
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Expired Verification Keys (default value is 3 days)
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# Use console backend for testing
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Email Configuration Settings
EMAIL_BACKEND = config("EMAIL_BACKEND", cast=str)
EMAIL_HOST = config("EMAIL_HOST", cast=str)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool, default=False)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", cast=str)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str)
DEFAULT_FROM_EMAIL = config(
    "DEFAULT_FROM_EMAIL", cast=str, default=config("EMAIL_HOST_USER")
)

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Use custom email templates
ACCOUNT_EMAIL_CONFIRMATION_TEMPLATE = "user_account/email/email_confirmation_message.txt"

# Use custom password reset templates
PASSWORD_RESET_TEMPLATE = "user_account/email/password_reset_key_message.txt"

# Custom Account Adapters Configuration
ACCOUNT_ADAPTER = "user_account.custom_adapters.CustomAccountAdapter"
