import os
basedir = os.path.abspath(os.path.dirname(__file__))

AUTH_USERS = 'authusers'

class Config(object):
    'Base config class'
    SECRET_KEY = '15acd65d26cfb615ed6983d2ba398b4b7f5038a9645c402e'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProdConfig(Config):
    'Production specific config'
    SECRET_KEY = '8cfebfbaefb1be12f0bb5ace0fa74bef187e48519ea3d0d1'

class StagingConfig(Config):
    'Staging specific config'
    DEBUG = True

class DevConfig(Config):
    'Development environment specific config'
    DEBUG = True
    SECRET_KEY = 'ece7088abd8e19b9e11f28e10cc6077c333ce224e0af8c5b'
    
