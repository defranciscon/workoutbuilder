import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    'Base config class'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProdConfig(Config):
    'Production specific config'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class StagingConfig(Config):
    'Staging specific config'
    DEBUG = True

class DevConfig(Config):
    'Development environment specific config'
    DEBUG = True
    SECRET_KEY = 'ece7088abd8e19b9e11f28e10cc6077c333ce224e0af8c5b'
    
