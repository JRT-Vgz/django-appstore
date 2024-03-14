from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    	    'default': {
                'ENGINE': 'django.db.backends.mysql',
        	    "OPTIONS": {
		        "read_default_file": "settings/mysql.cnf",   
		        }
    	    }
}

