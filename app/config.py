import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "this-really-needs-to-be-changed"
    JSON_SORT_KEYS = "False"
    
    # database
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    DB_USER = os.environ["DB_USER"]
    DB_PASS = os.environ["DB_PASS"]
    DB_NAME = os.environ["DB_NAME"]
    DB_URI  = os.environ["DB_URI"]
    DB_CONN = {
        "host"      : DB_HOST,
        "port"      : DB_PORT,
        "database"  : DB_NAME,
        "user"      : DB_USER,
        "password"  : DB_PASS
    }

    # database connection pooling
    DB_POOL_MINCONN = os.environ["DB_POOL_MINCONN"]
    DB_POOL_MAXCONN = os.environ["DB_POOL_MAXCONN"]



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
