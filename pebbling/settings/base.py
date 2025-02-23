from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",  # Stores Celery task results in DB
    "django_celery_beat",  # Enables periodic tasks
    "pebbling",
    "pebbling_apps.common",
    "pebbling_apps.users",
    "pebbling_apps.profiles",
    "pebbling_apps.bookmarks",
    "pebbling_apps.feeds",
    "pebbling_apps.home",
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

ROOT_URLCONF = "pebbling.urls"

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
                "pebbling_apps.users.context_processors.timezone_context",
            ],
        },
    },
]

WSGI_APPLICATION = "pebbling.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

_shared_sqlite_options = {
    "transaction_mode": "IMMEDIATE",
    "timeout": 5,  # seconds
    "init_command": """
        PRAGMA journal_mode=WAL;
        PRAGMA synchronous=NORMAL;
        PRAGMA mmap_size=134217728;
        PRAGMA journal_size_limit=27103364;
        PRAGMA cache_size=2000;
    """,
}

DATABASES_BASE_DIR = BASE_DIR / "data"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASES_BASE_DIR / "main.sqlite3",
        "OPTIONS": {
            **_shared_sqlite_options,
        },
    },
    "feeds_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASES_BASE_DIR / "feeds.sqlite3",
        "OPTIONS": {
            **_shared_sqlite_options,
        },
    },
    "celery_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASES_BASE_DIR / "celery.sqlite3",
        "OPTIONS": {
            **_shared_sqlite_options,
        },
    },
    "cache_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASES_BASE_DIR / "cache.sqlite3",
        "OPTIONS": {
            **_shared_sqlite_options,
        },
    },
}

DATABASE_ROUTERS = [
    "pebbling.routers.CacheRouter",
    "pebbling.routers.CeleryRouter",
    "pebbling.routers.FeedsRouter",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache_table",
        "OPTIONS": {
            "DATABASE": "cache_db",
        },
    }
}

# Celery settings
CELERY_BEAT_SCHEDULE_FILENAME = str(BASE_DIR / "data" / "celerybeat-schedule")
CELERY_BROKER_URL = (
    "sqla+sqlite:///data/celery.sqlite3"  # Use separate SQLite DB for Celery
)
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_EXTENDED = True

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

APPEND_SLASH = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "frontend/build",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

LOGIN_REDIRECT_URL = "profiles:index"

LOGOUT_REDIRECT_URL = "users:login"
