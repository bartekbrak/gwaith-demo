import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'dx&!90@j*5142uy@8bm=47i6v=d46-e5)9c&evd6azi2)xkr%s'
DEBUG = True
9
# apps and middlewares are cut down to absolute minimum disabling many features
# for brevity, in production env this should be configured differently
# as needed,
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'gwaithdemo',
    'rest_framework'
)
MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

# enough for demo, should be enough for production too, if proper
# backups are provided
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = 'static'


# Allows sqlite to understand timezone-aware datetimes that gwaith provides
USE_TZ = True
