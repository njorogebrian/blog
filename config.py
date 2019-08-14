import os
class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = "branjo124"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLCLCHEMY_RECORD_QUERIES = True
    CSRF_ENABLED = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.gmail.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','briannjoroge2000.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','november051999')
    MAIL_SENDER = os.environ.get('MAIL_SENDER', 'Project Admin<briannjoroge2000@gmail.com>')
    PROJECT_ADMIN = os.environ.get('PROJECT_ADMIN', 'PROJECT_ADMIN')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', False))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL',  True))
    MAIL_SUBJECT_PREFIX = '[PROJECT]'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:ps4@localhost/blog'
'

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:ps4@localhost/blog'
'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}
