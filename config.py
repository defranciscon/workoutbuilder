import os
basedir = os.path.abspath(os.path.dirname(__file__))

AUTH_USERS = 'authusers'

class Config(object):
    'Base config class'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProdConfig(Config):
    'Production specific config'
    SECRET_KEY = os.enviorn.get('SECRET_KEY')

class StagingConfig(Config):
    'Staging specific config'
    DEBUG = True

class DevConfig(Config):
    'Development environment specific config'
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
