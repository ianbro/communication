from .settings_general import *

# debug value is referenced in mail/forms.py to determine whether the mailer send function is called.
DEBUG = True

REDIS_HOST = "127.0.0.1"
REDIS_NAMES_DB = 9

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME'    : 'vagrant',                      # Or path to database file if using sqlite3.
        'USER'    : 'vagrant',                      # Not used with sqlite3.
        'PASSWORD': 'vagrant',                  # Not used with sqlite3.
        'HOST'    : '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT'    : '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'