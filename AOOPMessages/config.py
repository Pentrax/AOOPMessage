import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'AOOPMessages'
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = os.

class DevelopmentConfig(Config):

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'postgres://zbycceck:RT4QUFe70NCMFDYZKm3oMk2RdN9D68Zr@ruby.db.elephantsql.com:5432/zbycceck'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'postgres://gclvtktm:9L3H48BSQMq_ylo51VZSZzeqMO-EiIqd@isilo.db.elephantsql.com:5432/gclvtktm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}