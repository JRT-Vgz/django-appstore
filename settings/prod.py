from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    	    'default': {
                'ENGINE': 'django.db.backends.mysql',
        	    "OPTIONS": {
		        #"read_default_file": "my_store/mysql.cnf",   
		        }
    	    }
}
