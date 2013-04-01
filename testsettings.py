DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',  # For the User model
    'django.contrib.contenttypes',
    'django.contrib.sites', # For including the site name when dispatching. TODO: Should not be required.
    'south',
    'subscriptions',
)

SITE_ID = 1
USE_TZ = True
SECRET_KEY = 'secret key'
