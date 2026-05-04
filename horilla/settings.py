import os
from os.path import join
from pathlib import Path

import environ
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, "django-insecure-change-this"),
)

env.read_env(os.path.join(BASE_DIR, ".env"), overwrite=True)

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "notifications",
    "mathfilters",
    "corsheaders",
    "simple_history",
    "django_filters",
    "base",
    "employee",
    "recruitment",
    "leave",
    "pms",
    "onboarding",
    "asset",
    "attendance",
    "payroll",
    "widget_tweaks",
    "django_apscheduler",
]

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "horilla_api.middleware.RejectBasicAuthMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "horilla.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "horilla.wsgi.application"

if env("DATABASE_URL", default=None):
    DATABASES = {
        "default": env.db(),
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "TestDB_Horilla.sqlite3"),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

WHITENOISE_MANIFEST_STRICT = False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.DEBUG: "oh-alert--warning",
    messages.INFO: "oh-alert--info",
    messages.SUCCESS: "oh-alert--success",
    messages.WARNING: "oh-alert--warning",
    messages.ERROR: "oh-alert--danger",
}

LOGIN_URL = "/login"

SIMPLE_HISTORY_REVERT_DISABLED = True

DJANGO_NOTIFICATIONS_CONFIG = {
    "USE_JSONFIELD": True,
    "SOFT_DELETE": True,
    "USE_WATCHED": True,
    "NOTIFICATIONS_STORAGE": "notifications.storage.DatabaseStorage",
    "TEMPLATE": "notifications.html",
}

X_FRAME_OPTIONS = "SAMEORIGIN"

LANGUAGES = (
    ("en", "English (US)"),
    ("de", "Deutsche"),
    ("es", "Español"),
    ("fr", "Français"),
    ("ar", "عربى"),
    ("pt-br", "Português (Brasil)"),
    ("zh-hans", "Simplified Chinese"),
    ("zh-hant", "Traditional Chinese"),
    ("it", "Italian"),
)

LOCALE_PATHS = [
    join(BASE_DIR, "horilla", "locale"),
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = env("TIME_ZONE", default="Asia/Kolkata")

USE_I18N = True
USE_TZ = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")