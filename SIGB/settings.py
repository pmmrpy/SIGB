"""
Django settings for SIGB project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print "BASE_DIR path:", BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o5r=v1!o&c(er*9-b@yma0ja=-&20qic^(3t*&dj9w_7e@=i2u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'material',
    # 'material.frontend',
    # 'material.admin',
    # 'grappelli',
    'suit',
    'dal',
    'dal_select2',
    'admin_view_permission',
    # 'ajax_select',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'polymorphic',
    # 'controlcenter',
    'datetimewidget',
    'bar',
    'clientes',
    'compras',
    'personal',
    'stock',
    'ventas',
    'geraldo',
    # Prueba de calendarium
    'filer',
    'mptt',
    'easy_thumbnails',
    'calendarium',
    'input_mask',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SIGB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'material.frontend.context_processors.modules',
            ],
        },
    },
]

# Where are the Django source files?
# https://docs.djangoproject.com/en/1.8/intro/tutorial02/
# If you have difficulty finding where the Django source files are located on your system, run the following command:
#
# $ python -c "
# import sys
# sys.path = sys.path[1:]
# import django
# print(django.__path__)"
#
# ['C:\\Python27\\lib\\site-packages\\django']


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'SIGB Admin',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'SEARCH_URL': '',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #     'auth': 'icon-lock',
    #     'bar': 'icon-list',
    #     'clientes': 'icon-user',
    #     'compras': 'icon-shopping-cart',
    #     'personal': 'icon-flag',
    #     'stock': 'icon-cog',
    #     'ventas': 'icon-random',
    # },

    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU_EXCLUDE': ('filer',),
    'MENU': (
        'sites',
        {'app': 'auth', 'icon': 'icon-lock'},  # , 'models': ('user', 'group')
        # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        # {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
        {'app': 'bar', 'label': 'Parametrizaciones', 'icon': 'icon-list'},
        {'app': 'clientes', 'label': 'Clientes', 'icon': 'icon-user',
         'models': (
            'cliente', 'reserva',
            {'label': 'Calendario de Reservas', 'url': '/calendar/'},)
        },
        {'app': 'compras', 'label': 'Compras', 'icon': 'icon-shopping-cart'},
        {'app': 'personal', 'label': 'Personal', 'icon': 'icon-flag'},
        {'app': 'stock', 'label': 'Stock', 'icon': 'icon-cog'},
        {'app': 'ventas', 'label': 'Ventas', 'icon': 'icon-random'},
        #  {'label': 'Custom view', 'icon':'icon-cog', 'models': (
        #     {'label': 'Custom link', 'url': 'auth.user'},
        # )},

    ),

    # misc
    # 'LIST_PER_PAGE': 15
}

# CONTROLCENTER_DASHBOARDS = (
#     'SIGB.dashboards.MyDashboard',
# )


WSGI_APPLICATION = 'SIGB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# ===> PRODUCCION <===
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'SIGB',
#         'USER': 'sigbadmin',
#         'PASSWORD': 'sigbadmin',
#         'HOST': '',
#         'PORT': '',
#     }
# }

# ===> DESARROLLO <===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SIGB_desarrollo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-PY'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

NUMBER_GROUPING = 3

THOUSAND_SEPARATOR = '.'

DECIMAL_SEPARATOR = ','

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Your project will probably also have static assets that arent tied to a particular app. In addition to using a
# static/ directory inside your apps, you can define a list of directories (STATICFILES_DIRS) in your settings file
# where Django will also look for static files. For example:
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
# )