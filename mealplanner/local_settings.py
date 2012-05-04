from django.conf import global_settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

LOCAL_INSTALLED_APPS = (
        'debug_toolbar',
)

LOCAL_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES' : True,
}

GLOBAL_MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES = GLOBAL_MIDDLEWARE_CLASSES + LOCAL_MIDDLEWARE_CLASSES

GLOBAL_INSTALLED_APPS = global_settings.INSTALLED_APPS
#INSTALLED_APPS = GLOBAL_INSTALLED_APPS + LOCAL_INSTALLED_APPS
