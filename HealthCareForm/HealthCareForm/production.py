# production.py

from .settings import *

# Production-specific settings
DEBUG = False


LOGGING['handlers']['file']['level'] = 'INFO'  

LOGGING['handlers']['security_file']['level'] = 'WARNING'  
LOGGING['loggers']['django.security']['level'] = 'WARNING'  

