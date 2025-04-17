import os 

from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ("HOST_DB"),
        'PORT': os.environ("PORT_DB"),
        'NAME': os.environ("NAME_DB"),
        'USER': os.environ("USER_DB"),
        'PASSWORD': os.environ("PASSWORD_DB"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
