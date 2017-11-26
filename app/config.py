import os


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    PORT = os.environ['PORT']


class DevConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass